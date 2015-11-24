import six
html_equity = """      
	<div class="historic-bar" style="width:950px; margin-bottom:5px;"><span><nobr>Data for SBIN - EQ from Nov 07, 2015 to Nov 13, 2015</nobr></span> <span class="download-data-link"><a href="/content/equities/scripvol/datafiles/07-11-2015-TO-13-11-2015SBINEQN.csv" target="_blank" style="text:align:right;">Download file in csv format</a></span></div>

		  <table border="0" cellpadding="4" cellspacing="1" bgcolor="#969696" width="950">
		  <tr style="height:20">	  
		  <th nowrap>Symbol</th>
		  <th nowrap>Series</th>
		  <th nowrap>Date</td>
		  <th nowrap>Prev Close</th>
		  <th nowrap>Open Price</th>
		  <th nowrap>High Price</th>
		  <th nowrap>Low Price</th>
		  <th nowrap>Last Price</th>
		  <th nowrap>Close Price</th>
		  <th nowrap>VWAP</th>
		  <th nowrap>Total Traded<br /> Quantity</th>
		  <th nowrap>Turnover<br /><img src="/images/rup_t1.gif" alt="Rs." border="0"/> in Lacs</th>
		  <th nowrap>No. of <br />Trades</th>
		  <th nowrap>Deliverable<br />Qty</th>
		  <th nowrap>% Dly Qt to<br />Traded Qty</th>
		  </tr>	  
			  
			  <tr>
			  
							  <td class="normalText" nowrap>SBIN</td>


			  <td class="normalText" nowrap>EQ</td>

			 
				<td class="date" nowrap>09-Nov-2015</td>		
				


				 

		

			   
			  <td class="number" nowrap>243.00</td>
			  
			  <td class="number" nowrap>236.00</td>
			  
			  <td class="number" nowrap>248.30</td>
			  
			  <td class="number" nowrap>235.60</td>
			  
			  <td class="number" nowrap>245.65</td>
			  
			  <td class="number" nowrap>246.10</td>
			  
			  <td class="number" nowrap>244.83</td>
			  
			  <td class="number" nowrap>2,28,06,485</td>
			  
			  <td class="number" nowrap>55,838.06</td>
			  
			  <td class="number" nowrap>1,69,076</td>
			  
			  <td class="number" nowrap>86,69,018</td>
			  
			  <td class="number" nowrap>38.01</td>
			  
			  </tr>
			  
			  <tr>
			  
							  <td class="normalText" nowrap>SBIN</td>


			  <td class="normalText" nowrap>EQ</td>

			 
				<td class="date" nowrap>10-Nov-2015</td>		
				


				 

		

			   
			  <td class="number" nowrap>246.10</td>
			  
			  <td class="number" nowrap>244.90</td>
			  
			  <td class="number" nowrap>247.25</td>
			  
			  <td class="number" nowrap>240.10</td>
			  
			  <td class="number" nowrap>241.30</td>
			  
			  <td class="number" nowrap>241.20</td>
			  
			  <td class="number" nowrap>243.15</td>
			  
			  <td class="number" nowrap>1,17,67,845</td>
			  
			  <td class="number" nowrap>28,613.54</td>
			  
			  <td class="number" nowrap>81,141</td>
			  
			  <td class="number" nowrap>28,45,909</td>
			  
			  <td class="number" nowrap>24.18</td>
			  
			  </tr>
			  
			  <tr>
			  
							  <td class="normalText" nowrap>SBIN</td>


			  <td class="normalText" nowrap>EQ</td>

			 
				<td class="date" nowrap>11-Nov-2015</td>		
				


				 

		

			   
			  <td class="number" nowrap>241.20</td>
			  
			  <td class="number" nowrap>243.00</td>
			  
			  <td class="number" nowrap>244.25</td>
			  
			  <td class="number" nowrap>242.55</td>
			  
			  <td class="number" nowrap>243.20</td>
			  
			  <td class="number" nowrap>243.15</td>
			  
			  <td class="number" nowrap>243.28</td>
			  
			  <td class="number" nowrap>20,61,681</td>
			  
			  <td class="number" nowrap>5,015.68</td>
			  
			  <td class="number" nowrap>24,738</td>
			  
			  <td class="number" nowrap>8,30,764</td>
			  
			  <td class="number" nowrap>40.30</td>
			  
			  </tr>
			  
			  <tr>
			  
							  <td class="normalText" nowrap>SBIN</td>


			  <td class="normalText" nowrap>EQ</td>

			 
				<td class="date" nowrap>13-Nov-2015</td>		
				


				 

		

			   
			  <td class="number" nowrap>243.15</td>
			  
			  <td class="number" nowrap>241.50</td>
			  
			  <td class="number" nowrap>241.80</td>
			  
			  <td class="number" nowrap>237.70</td>
			  
			  <td class="number" nowrap>240.30</td>
			  
			  <td class="number" nowrap>240.25</td>
			  
			  <td class="number" nowrap>239.92</td>
			  
			  <td class="number" nowrap>90,82,062</td>
			  
			  <td class="number" nowrap>21,789.37</td>
			  
			  <td class="number" nowrap>68,168</td>
			  
			  <td class="number" nowrap>27,16,416</td>
			  
			  <td class="number" nowrap>29.91</td>
			  
			  </tr>
		  
		  </table>	 

		<!-- <tr><td class="smalllinks" style="text-align:right" > <br /> -->
		<!-- <a href="/content/equities/scripvol/datafiles/07-11-2015-TO-13-11-2015SBINEQN.csv" target="_blank">Download file in csv format</a></td></tr> -->	

	<!--Content Area Ends Here-->
	"""
csv_equity = """
SBIN,EQ,09-Nov-2015,243,236,248.3,235.6,245.65,246.1,244.83,22806485,55838.06,169076,8669018,38.01
SBIN,EQ,10-Nov-2015,246.1,244.9,247.25,240.1,241.3,241.2,243.15,11767845,28613.54,81141,2845909,24.18
SBIN,EQ,11-Nov-2015,241.2,243,244.25,242.55,243.2,243.15,243.28,2061681,5015.68,24738,830764,40.3
SBIN,EQ,13-Nov-2015,243.15,241.5,241.8,237.7,240.3,240.25,239.92,9082062,21789.37,68168,2716416,29.91
"""
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

unzipped = "'Quantum mechanics was developed in the 1920s and 1930s because classical physics could not explain  the stability of atoms.  In particular, classical electromagnetic theory predicted that if negatively charged electrons were orbiting a positively charged nucleus, the electrons would continuously emit electromagnetic radiation (light) and would quickly fall into the nucleus.  There was also no explanation about why atoms emitted light at discrete frequencies.  Quantum theory could explain the stability of atoms and could explain many other fact that classical physics could not explain, such as the black body spectrum and the photoelectric effect.'"
zipped = 'PK\x03\x04\x14\x00\x00\x00\x08\x00=\trGa\x95|\x06M\x01\x00\x00\x8f\x02\x00\x00\x07\x00\x00\x00zip.txt\x8dQKN\xc3@\x0c\xbd\x8aw\x80TU|V\x1c\x81%\x12\x17pf\x9c\xc4\xead\x9c\x8e=\x94\xdc\x1eO\x12\xa4\xaa\x08\x89\x9de\xfb}\xfc|\xf7^1[\x9d`\xa20b\xe6\xa0pA\x85H\x9f\x94d\xa6\x08\x9c\xc1F\x82\xa7\xd7\xe7G\x05\xcc\xd1\xab\x17\xaf:\nX\x95 $T\xe5\x80\t\xe6q\xd1\x06\x0fRS\x84,\x06\xf45\'t\xfcJ\xa0\x86\x1d\'\xb6\x05\xa4\x074\x99\xf4\x08\xf0\x96a\xc6b\x1cj\xc2r\xb8"\xa3D\xc1\x8aL8d\xf2qc\x90\xb2\xc0\\(r0\x8a\xde@\x03\xee!\xd3\x80\xc6nv\x01\xf7_\x06\x1f\xed\xd8\xec\x97P!\x90\xd2\xb1q\x1e\x00a\x16\xe5\x9b\xe5\\C\xa2\xaa\x87\xa6p\x8dlG\xf8)\xd9\x91U\xaa:\x82&\xb6_\xbe\nFv}\xc9p\x9fx\x18\xed\xa1E\xb4\xa3\xcf\x95\xc3\xc9\x81=\xa6\xe41\x9a4\x8d]\xb0\x1d\xff1\xba\xbd5mL*\x9e\xd8\x16X\xde\xf8\xb0\x93jp\x19\x97-\xacU\xbe\x1d\xbe\xcax\x0f"k(d\x04}\xa1s\xa5\x1c\x98\x1a\xeb\xfe\xcf=\xb1\xed\x1b?\x9f\xf8\xe3\x11\xcd\xf3\xcd\xe2\x84\xd9\xe7\xbe^\xdc~\xb05\xee\xff\xfc\xfa\x00Z\xc3\x08\xa8\xabT\x970\x9c\xa0\x93\xb8\x80\xce-\xb8:5\xad6s\n1\xd9\xe2\xf4\x1c\xa9\xef\xbd:\xde}\x03PK\x01\x02?\x00\x14\x00\x00\x00\x08\x00=\trGa\x95|\x06M\x01\x00\x00\x8f\x02\x00\x00\x07\x00$\x00\x00\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00zip.txt\n\x00 \x00\x00\x00\x00\x00\x01\x00\x18\x00Y\xd8\xfb\xbco!\xd1\x01Z\xb3\xb0\xb7o!\xd1\x01Z\xb3\xb0\xb7o!\xd1\x01PK\x05\x06\x00\x00\x00\x00\x01\x00\x01\x00Y\x00\x00\x00r\x01\x00\x00\x00\x00'
'''
fp = open('zip.zip','wb')
fp.write(zipped)
fp.close()
'''


        
