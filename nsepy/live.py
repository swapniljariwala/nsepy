# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 21:51:41 2015

@author: SW274998
"""
from nsepy.commons import *
import ast
import json
from nsepy.liveurls import *

def _parse_get_quote(text):
    
    match = re.search(\
                        r'\{<div\s+id="responseDiv"\s+style="display:none">\s+(\{.*?\{.*?\}.*?\})',
                        text, re.S
                    )
            # ast can raise SyntaxError, let's catch only this error
    try:
        buffer = match.group(1)
        buffer = js_adaptor(buffer)
        response = _clean_server_response(ast.literal_eval(buffer)['data'][0])
    except SyntaxError as err:
        raise Exception('ill formatted response')
    else:
        return _render_response(response, as_json)
    
def _render_response(self, data, as_json=False):
        if as_json is True:
            return json.dumps(data)
        else:
            return data
            
def _clean_server_response(resp_dict):
        """cleans the server reponse by replacing:
            '-'     -> None
            '1,000' -> 1000
        :param resp_dict:
        :return: dict with all above substitution
        """

        # change all the keys from unicode to string
        d = {}
        for key, value in resp_dict.items():
            d[str(key)] = value
        resp_dict = d
        for key, value in resp_dict.items():
            if type(value) is str or isinstance(value, six.string_types):
                if re.match('-', value):
                    resp_dict[key] = None
                elif re.search(r'^[0-9,.]+$', value):
                    # replace , to '', and type cast to int
                    resp_dict[key] = float(re.sub(',', '', value))
                else:
                    resp_dict[key] = str(value)
        return resp_dict

