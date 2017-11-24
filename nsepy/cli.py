import click
from .history import get_history, get_index_pe_history
from datetime import datetime

def print_help_msg(command):
    with click.Context(command) as ctx:
        click.echo(command.get_help(ctx))

@click.group()
@click.option('--debug/--no-debug', default=False)
def cli(debug):
    if debug:
        click.echo('Debug mode is %s' % ('on' if debug else 'off'))

@click.command()
@click.option('--symbol', '-S',  help='Security code')
@click.option('--start', '-s', help='Start date in yyyy-mm-dd format')
@click.option('--end', '-e', help='End date in yyyy-mm-dd format')
@click.option('--series', default='EQ', help='Default series - EQ')
@click.option('--file', '-o', 'file_name',  help='Output file name')
@click.option('--index/--no-index', default=False, help='--index if security is index else --no-index')
@click.option('--futures/--no-futures', default=False, help='--futures for futures derivative else --no-futures')
@click.option('--expiry', default=None, help='Expiry date in yyyy-mm-dd')
@click.option('--opt-type', 'option_type', default="", type=click.Choice(['CE', 'PE', 'CA', 'PA', '']),
                help='Option type, CE - European call, PE - European put, CA - American call, PA - American put, (Leave blank for futures derivatives and non-derivative securities)')
@click.option('--strike', default="", help='Strike price for option derivatives')
@click.option('--format', '-f', default='csv',  type=click.Choice(['csv', 'pkl']),
                help='Output format, pkl - to save as Pickel and csv - to save as csv')
def history(symbol, start, end, series, file_name, index, futures, expiry, option_type, strike, format):
    try:
        sd = datetime.strptime(start, "%Y-%m-%d").date()
        ed = datetime.strptime(end, "%Y-%m-%d").date()
    except:
        click.secho("Please provide start and end date in format yyyy-mm-dd", fg='red', nl=True)
        print_help_msg(history)
        return
    if not symbol:
        click.secho("Please provide security/index code", fg='red', nl=True)
        print_help_msg(history)
        return

    if expiry:
        exd = datetime.strptime(expiry, "%Y-%m-%d").date()
    else:
        exd = None
    if strike:
        strike_price = float(strike)
    else:
        strike_price = ""

    df = get_history(symbol, sd, ed, index, futures, option_type,
                        exd, strike_price, series)
    click.echo(df.head())
    if not file_name:
        file_name = symbol + '.' + format
    if format == 'csv':
        df.to_csv(file_name)
    else:
        df.to_pickle(file_name)
    click.secho('Saved to: {}'.format(file_name), fg='green', nl=True)

@click.command()
@click.option('--symbol', '-S',  help='Index code')
@click.option('--start', '-s', help='Start date in yyyy-mm-dd format')
@click.option('--end', '-e', help='End date in yyyy-mm-dd format')
@click.option('--format', '-f', default='csv',  type=click.Choice(['csv', 'pkl']),
                help='Output format, pkl - to save as Pickel and csv - to save as csv')
@click.option('--file', '-o', 'file_name',  help='Output file name')
def pehistory(symbol, start, end, format, file_name):
    try:
        sd = datetime.strptime(start, "%Y-%m-%d").date()
        ed = datetime.strptime(end, "%Y-%m-%d").date()
    except:
        click.secho("\nPlease provide start and end date in format yyyy-mm-dd\n", fg='red')
        print_help_msg(pehistory)
        return
    if not symbol:
        click.secho("\nPlease provide security/index code\n", fg='red')
        print_help_msg(pehistory)
        return
    df = get_index_pe_history(symbol, sd, ed)
    click.echo(df.head())
    
    if not file_name:
        file_name = symbol + '.' + format

    if format == 'csv':
        df.to_csv(file_name)
    else:
        df.to_pickle(file_name)
    click.secho('Saved to: {}'.format(file_name) , fg='green', nl=True)


cli.add_command(history)
cli.add_command(pehistory)
if __name__ == '__main__':
    cli()
