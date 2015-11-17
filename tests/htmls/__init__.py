from .equity_html import html_equity
from .equity_csv import csv_equity
csv_index = """
02-Nov-2015,8054.55,8060.7,7995.6,8050.8,140323983,6552.67
03-Nov-2015,8086.35,8100.35,8031.75,8060.7,136625382,5955.64
04-Nov-2015,8104.9,8116.1,8027.3,8040.2,125935846,5696.01
05-Nov-2015,8030.35,8031.2,7944.1,7955.45,136223827,6001.38
06-Nov-2015,7956.55,8002.65,7926.15,7954.3,226329409,8771.77
09-Nov-2015,7788.25,7937.75,7771.7,7915.2,218422388,9376.17
10-Nov-2015,7877.6,7885.1,7772.85,7783.35,170267413,7153.47
11-Nov-2015,7838.8,7847.95,7819.1,7825,22380435,1123.44
13-Nov-2015,7762.45,7775.1,7730.9,7762.25,165876819,7731.55
"""
html_index = """
<!--VAPT Azhar-->

<!--VAPT Azhar-->












<table>
<tr><th colspan="7" class="tablehead">
Historical Data for NIFTY 50
</th></tr>

<tr><th colspan="7" class="tablehead">
For the period 02-11-2015 to 16-11-2015
</th></tr>



         <tr>
         
         <th >Date</th>
         <th >Open</th>
         <th >High</th>
         <th >Low</th>
         <th >Close</th>

           <th>Shares Traded</th>
           <th >Turnover <br/>(<!--Rs.--> <img src="/images/rup_t1.gif" alt = "Rs." border="0"> Cr)</th>

     </tr>

                  <tr>
                  <td class="date"><nobr>02-Nov-2015</nobr></td>
                  <td class="number">     8054.55</td>
                  <td class="number">     8060.70</td>
                  <td class="number">     7995.60</td>
                  <td class="number">     8050.80</td>


            <td class="number">      140323983</td>
                        <td class="number">         6552.67</td>

                  </tr>

                  <tr>
                  <td class="date"><nobr>03-Nov-2015</nobr></td>
                  <td class="number">     8086.35</td>
                  <td class="number">     8100.35</td>
                  <td class="number">     8031.75</td>
                  <td class="number">     8060.70</td>


            <td class="number">      136625382</td>
                        <td class="number">         5955.64</td>

                  </tr>

                  <tr>
                  <td class="date"><nobr>04-Nov-2015</nobr></td>
                  <td class="number">     8104.90</td>
                  <td class="number">     8116.10</td>
                  <td class="number">     8027.30</td>
                  <td class="number">     8040.20</td>


            <td class="number">      125935846</td>
                        <td class="number">         5696.01</td>

                  </tr>

                  <tr>
                  <td class="date"><nobr>05-Nov-2015</nobr></td>
                  <td class="number">     8030.35</td>
                  <td class="number">     8031.20</td>
                  <td class="number">     7944.10</td>
                  <td class="number">     7955.45</td>


            <td class="number">      136223827</td>
                        <td class="number">         6001.38</td>

                  </tr>

                  <tr>
                  <td class="date"><nobr>06-Nov-2015</nobr></td>
                  <td class="number">     7956.55</td>
                  <td class="number">     8002.65</td>
                  <td class="number">     7926.15</td>
                  <td class="number">     7954.30</td>


            <td class="number">      226329409</td>
                        <td class="number">         8771.77</td>

                  </tr>

                  <tr>
                  <td class="date"><nobr>09-Nov-2015</nobr></td>
                  <td class="number">     7788.25</td>
                  <td class="number">     7937.75</td>
                  <td class="number">     7771.70</td>
                  <td class="number">     7915.20</td>


            <td class="number">      218422388</td>
                        <td class="number">         9376.17</td>

                  </tr>

                  <tr>
                  <td class="date"><nobr>10-Nov-2015</nobr></td>
                  <td class="number">     7877.60</td>
                  <td class="number">     7885.10</td>
                  <td class="number">     7772.85</td>
                  <td class="number">     7783.35</td>


            <td class="number">      170267413</td>
                        <td class="number">         7153.47</td>

                  </tr>

                  <tr>
                  <td class="date"><nobr>11-Nov-2015</nobr></td>
                  <td class="number">     7838.80</td>
                  <td class="number">     7847.95</td>
                  <td class="number">     7819.10</td>
                  <td class="number">     7825.00</td>


            <td class="number">       22380435</td>
                        <td class="number">         1123.44</td>

                  </tr>

                  <tr>
                  <td class="date"><nobr>13-Nov-2015</nobr></td>
                  <td class="number">     7762.45</td>
                  <td class="number">     7775.10</td>
                  <td class="number">     7730.90</td>
                  <td class="number">     7762.25</td>


            <td class="number">      165876819</td>
                        <td class="number">         7731.55</td>

                  </tr>

  
   


        <tr><td align="right" colspan="7">
        <a href="/content/indices/histdata/NIFTY 5002-11-2015-16-11-2015.csv" target="_blank">Download file in csv format</a>
        </td></tr>


</table>

"""
csv_derivative = """
NIFTY,09-Nov-2015,26-Nov-2015,7820.00,7954.90,7790.00,7936.05,7937.95,7936.05,226372,1336309.59,17932575,-739725,7915.20
NIFTY,10-Nov-2015,26-Nov-2015,7895.35,7908.00,7791.15,7802.50,7800.00,7802.50,158968,935549.88,17737575,-195000,7783.35
NIFTY,11-Nov-2015,26-Nov-2015,7860.00,7860.00,7812.00,7825.05,7828.05,7825.05,23566,138245.49,17633325,-104250,7825.00
NIFTY,13-Nov-2015,26-Nov-2015,7765.90,7797.40,7742.55,7774.30,7770.00,7774.30,113362,660725.42,17551350,-81975,7762.25
"""

html_derivative = """
 




 






  
 

	<div style="width: 760px; margin-bottom: 5px;" class="historic-bar"><span><nobr>Data for FUTIDX-NIFTY from 07-11-2015 to 13-11-2015</nobr></span> <span class="download-data-link"><a style="" target="_blank" href="/content/fo/contractvol/datafiles/FUTIDX_NIFTY_07-11-2015_TO_13-11-2015.csv" target="_blank">Download file in csv format</a></span></div>

	<table>
	<tr><th  colspan="17">Historical Contract-wise Price Volume Data</th></tr>
	<!--<tr><td class="tablehead"  colspan="15">Data for FUTIDX-NIFTY from 07-11-2015 to 13-11-2015</td ></tr>-->
	
	<tr>
	
	<th>Symbol </th>
	<th class="tablehead"  >Date </th >
	<th class="tablehead"  >Expiry</th>
	

	<th  >Open</th >
	<th  >High</th >
	<th  >Low</th >
	<th  >Close</th >
	<th  >LTP</th >
	<th  >Settle Price</th >
	<th  >No. of contracts</th >
	<th  >Turnover * <br /> in <img src="/images/rup_t1.gif" alt="Rs." border="0"/> Lacs</th >

    <th  >Open Int</th >
	<th  >Change in OI</th >
	<th  >Underlying Value</th >
	</tr>
	
 
	  <tr>
	  <td class="normalText">NIFTY</td>
	  <td class="date"><nobr>09-Nov-2015</nobr></td>
	  <td class="date"> <nobr>26-Nov-2015</nobr></td>
	  

	  <td class="number">7,820.00</td>
	  <td class="number">7,954.90</td>
	  <td class="number">7,790.00</td>
	  <td class="number">7,936.05</td>
	  <td class="number">7,937.95</td>
	  <td class="number">7,936.05</td>
	  <td class="number">2,26,372</td>
	  <td class="number">13,36,309.59</td>

	  <td class="number">1,79,32,575</td>
	  <td class="number">-7,39,725</td>
	  <!-- Changed by Ruchira for 2 to 4 decimal changes on 2/24/2014-->
	  <td class="number">7,915.20</td>
	  </tr>
 
	  <tr>
	  <td class="normalText">NIFTY</td>
	  <td class="date"><nobr>10-Nov-2015</nobr></td>
	  <td class="date"> <nobr>26-Nov-2015</nobr></td>
	  

	  <td class="number">7,895.35</td>
	  <td class="number">7,908.00</td>
	  <td class="number">7,791.15</td>
	  <td class="number">7,802.50</td>
	  <td class="number">7,800.00</td>
	  <td class="number">7,802.50</td>
	  <td class="number">1,58,968</td>
	  <td class="number">9,35,549.88</td>

	  <td class="number">1,77,37,575</td>
	  <td class="number">-1,95,000</td>
	  <!-- Changed by Ruchira for 2 to 4 decimal changes on 2/24/2014-->
	  <td class="number">7,783.35</td>
	  </tr>
 
	  <tr>
	  <td class="normalText">NIFTY</td>
	  <td class="date"><nobr>11-Nov-2015</nobr></td>
	  <td class="date"> <nobr>26-Nov-2015</nobr></td>
	  

	  <td class="number">7,860.00</td>
	  <td class="number">7,860.00</td>
	  <td class="number">7,812.00</td>
	  <td class="number">7,825.05</td>
	  <td class="number">7,828.05</td>
	  <td class="number">7,825.05</td>
	  <td class="number">23,566</td>
	  <td class="number">1,38,245.49</td>

	  <td class="number">1,76,33,325</td>
	  <td class="number">-1,04,250</td>
	  <!-- Changed by Ruchira for 2 to 4 decimal changes on 2/24/2014-->
	  <td class="number">7,825.00</td>
	  </tr>
 
	  <tr>
	  <td class="normalText">NIFTY</td>
	  <td class="date"><nobr>13-Nov-2015</nobr></td>
	  <td class="date"> <nobr>26-Nov-2015</nobr></td>
	  

	  <td class="number">7,765.90</td>
	  <td class="number">7,797.40</td>
	  <td class="number">7,742.55</td>
	  <td class="number">7,774.30</td>
	  <td class="number">7,770.00</td>
	  <td class="number">7,774.30</td>
	  <td class="number">1,13,362</td>
	  <td class="number">6,60,725.42</td>

	  <td class="number">1,75,51,350</td>
	  <td class="number">-81,975</td>
	  <!-- Changed by Ruchira for 2 to 4 decimal changes on 2/24/2014-->
	  <td class="number">7,762.25</td>
	  </tr>

	

<!--	<tr><td class="smalllinks" align="right" colspan="14"> <a href="/content/fo/contractvol/datafiles/FUTIDX_NIFTY_07-11-2015_TO_13-11-2015.csv" target="_blank" >Download file in csv format</a></td></tr> -->
	
</table>
<br/>
<br/>
<div  >
			<p class="title">Note: <br/>
			*  In case of Option Contracts "Turnover" represents "Notional Turnover" <br/>
			** Premium Turnover is calculated w.e.f. September 01, 2015 </p>
</div>	

     

"""
