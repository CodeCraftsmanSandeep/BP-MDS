# Input Instances

Capacity-only CVRP benchmarks from CVRPLIB, FILO2, and Synthetic XML-style instances *(CVRPLIB accessed 25 July 2026)*.

**320** instances &nbsp;·&nbsp; **CVRPLIB** 129 &nbsp;·&nbsp; **FILO2** 20 &nbsp;·&nbsp; **Synthetic** 171

Machine-readable index: [`instances.csv`](instances.csv)

---

## Instances

| Symbol | Meaning |
|:------:|:--------|
| **Size** | By **#Customers** (`N−1`): $\color{green}{\textsf{XS}}$ 1–100 · $\color{olive}{\textsf{S}}$ 101–1,000 · $\color{purple}{\textsf{M}}$ 1,001–10,000 · $\color{orange}{\textsf{L}}$ 10,001–50,000 · $\color{red}{\textsf{XL}}$ 50,001–100,000 · $\color{teal}{\textsf{XXL}}$ 100,001–1,000,000 · $\color{magenta}{\textsf{XXXL}}$ 1,000,001–10,000,000 |
| **Source** | `CVRPLIB` · `FILO2` · `Synthetic` |
| **Instance** | Clickable path under the source |
| **N** | `#Customers + 1` (= `DIMENSION`, includes depot) |
| **Q** | Vehicle capacity |
| **BKS** | Best-known solution cost (if available) |

<table>
<thead>
<tr>
<th align="right">S.No</th>
<th align="center">Size</th>
<th align="left">Source</th>
<th align="left">Instance</th>
<th align="right">N</th>
<th align="right">Q</th>
<th align="right">BKS</th>
</tr>
</thead>
<tbody>
<tr>
<td align="right">1</td>
<td align="center" rowspan="17">$\color{green}{\textsf{XS}}$</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML10_1173_01.vrp">XML10_1173_01</a></td>
<td align="right">11</td>
<td align="right">47</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">2</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML10_1176_01.vrp">XML10_1176_01</a></td>
<td align="right">11</td>
<td align="right">148</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">3</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML10_2173_01.vrp">XML10_2173_01</a></td>
<td align="right">11</td>
<td align="right">45</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">4</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML10_2176_01.vrp">XML10_2176_01</a></td>
<td align="right">11</td>
<td align="right">142</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">5</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/CMT/CMT1.vrp">CMT/CMT1</a></td>
<td align="right">51</td>
<td align="right">160</td>
<td align="right">524.611</td>
</tr>
<tr>
<td align="right">6</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML50_1173_01.vrp">XML50_1173_01</a></td>
<td align="right">51</td>
<td align="right">134</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">7</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML50_1176_01.vrp">XML50_1176_01</a></td>
<td align="right">51</td>
<td align="right">182</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">8</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML50_2173_01.vrp">XML50_2173_01</a></td>
<td align="right">51</td>
<td align="right">142</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">9</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML50_2176_01.vrp">XML50_2176_01</a></td>
<td align="right">51</td>
<td align="right">171</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">10</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/CMT/CMT2.vrp">CMT/CMT2</a></td>
<td align="right">76</td>
<td align="right">140</td>
<td align="right">835.262</td>
</tr>
<tr>
<td align="right">11</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/CMT/CMT12.vrp">CMT/CMT12</a></td>
<td align="right">101</td>
<td align="right">200</td>
<td align="right">819.558</td>
</tr>
<tr>
<td align="right">12</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/CMT/CMT3.vrp">CMT/CMT3</a></td>
<td align="right">101</td>
<td align="right">200</td>
<td align="right">826.137</td>
</tr>
<tr>
<td align="right">13</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n101-k25.vrp">X/X-n101-k25</a></td>
<td align="right">101</td>
<td align="right">206</td>
<td align="right">27591</td>
</tr>
<tr>
<td align="right">14</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML100_1173_01.vrp">XML100_1173_01</a></td>
<td align="right">101</td>
<td align="right">139</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">15</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML100_1176_01.vrp">XML100_1176_01</a></td>
<td align="right">101</td>
<td align="right">215</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">16</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML100_2173_01.vrp">XML100_2173_01</a></td>
<td align="right">101</td>
<td align="right">138</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">17</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML100_2176_01.vrp">XML100_2176_01</a></td>
<td align="right">101</td>
<td align="right">211</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">18</td>
<td align="center" rowspan="137">$\color{olive}{\textsf{S}}$</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n106-k14.vrp">X/X-n106-k14</a></td>
<td align="right">106</td>
<td align="right">600</td>
<td align="right">26362</td>
</tr>
<tr>
<td align="right">19</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n110-k13.vrp">X/X-n110-k13</a></td>
<td align="right">110</td>
<td align="right">66</td>
<td align="right">14971</td>
</tr>
<tr>
<td align="right">20</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n115-k10.vrp">X/X-n115-k10</a></td>
<td align="right">115</td>
<td align="right">169</td>
<td align="right">12747</td>
</tr>
<tr>
<td align="right">21</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n120-k6.vrp">X/X-n120-k6</a></td>
<td align="right">120</td>
<td align="right">21</td>
<td align="right">13332</td>
</tr>
<tr>
<td align="right">22</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/CMT/CMT11.vrp">CMT/CMT11</a></td>
<td align="right">121</td>
<td align="right">200</td>
<td align="right">1042.12</td>
</tr>
<tr>
<td align="right">23</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n125-k30.vrp">X/X-n125-k30</a></td>
<td align="right">125</td>
<td align="right">188</td>
<td align="right">55539</td>
</tr>
<tr>
<td align="right">24</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n129-k18.vrp">X/X-n129-k18</a></td>
<td align="right">129</td>
<td align="right">39</td>
<td align="right">28940</td>
</tr>
<tr>
<td align="right">25</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n134-k13.vrp">X/X-n134-k13</a></td>
<td align="right">134</td>
<td align="right">643</td>
<td align="right">10916</td>
</tr>
<tr>
<td align="right">26</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n139-k10.vrp">X/X-n139-k10</a></td>
<td align="right">139</td>
<td align="right">106</td>
<td align="right">13590</td>
</tr>
<tr>
<td align="right">27</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n143-k7.vrp">X/X-n143-k7</a></td>
<td align="right">143</td>
<td align="right">1190</td>
<td align="right">15700</td>
</tr>
<tr>
<td align="right">28</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n148-k46.vrp">X/X-n148-k46</a></td>
<td align="right">148</td>
<td align="right">18</td>
<td align="right">43448</td>
</tr>
<tr>
<td align="right">29</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/CMT/CMT4.vrp">CMT/CMT4</a></td>
<td align="right">151</td>
<td align="right">200</td>
<td align="right">1028.42</td>
</tr>
<tr>
<td align="right">30</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n153-k22.vrp">X/X-n153-k22</a></td>
<td align="right">153</td>
<td align="right">144</td>
<td align="right">21220</td>
</tr>
<tr>
<td align="right">31</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n157-k13.vrp">X/X-n157-k13</a></td>
<td align="right">157</td>
<td align="right">12</td>
<td align="right">16876</td>
</tr>
<tr>
<td align="right">32</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n162-k11.vrp">X/X-n162-k11</a></td>
<td align="right">162</td>
<td align="right">1174</td>
<td align="right">14138</td>
</tr>
<tr>
<td align="right">33</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n167-k10.vrp">X/X-n167-k10</a></td>
<td align="right">167</td>
<td align="right">133</td>
<td align="right">20557</td>
</tr>
<tr>
<td align="right">34</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n172-k51.vrp">X/X-n172-k51</a></td>
<td align="right">172</td>
<td align="right">161</td>
<td align="right">45607</td>
</tr>
<tr>
<td align="right">35</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n176-k26.vrp">X/X-n176-k26</a></td>
<td align="right">176</td>
<td align="right">142</td>
<td align="right">47812</td>
</tr>
<tr>
<td align="right">36</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n181-k23.vrp">X/X-n181-k23</a></td>
<td align="right">181</td>
<td align="right">8</td>
<td align="right">25569</td>
</tr>
<tr>
<td align="right">37</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n186-k15.vrp">X/X-n186-k15</a></td>
<td align="right">186</td>
<td align="right">974</td>
<td align="right">24145</td>
</tr>
<tr>
<td align="right">38</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n190-k8.vrp">X/X-n190-k8</a></td>
<td align="right">190</td>
<td align="right">138</td>
<td align="right">16980</td>
</tr>
<tr>
<td align="right">39</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n195-k51.vrp">X/X-n195-k51</a></td>
<td align="right">195</td>
<td align="right">181</td>
<td align="right">44225</td>
</tr>
<tr>
<td align="right">40</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/CMT/CMT5.vrp">CMT/CMT5</a></td>
<td align="right">200</td>
<td align="right">200</td>
<td align="right">1291.289144</td>
</tr>
<tr>
<td align="right">41</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n200-k36.vrp">X/X-n200-k36</a></td>
<td align="right">200</td>
<td align="right">402</td>
<td align="right">58578</td>
</tr>
<tr>
<td align="right">42</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n204-k19.vrp">X/X-n204-k19</a></td>
<td align="right">204</td>
<td align="right">836</td>
<td align="right">19565</td>
</tr>
<tr>
<td align="right">43</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n209-k16.vrp">X/X-n209-k16</a></td>
<td align="right">209</td>
<td align="right">101</td>
<td align="right">30656</td>
</tr>
<tr>
<td align="right">44</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n214-k11.vrp">X/X-n214-k11</a></td>
<td align="right">214</td>
<td align="right">944</td>
<td align="right">10856</td>
</tr>
<tr>
<td align="right">45</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n219-k73.vrp">X/X-n219-k73</a></td>
<td align="right">219</td>
<td align="right">3</td>
<td align="right">117595</td>
</tr>
<tr>
<td align="right">46</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n223-k34.vrp">X/X-n223-k34</a></td>
<td align="right">223</td>
<td align="right">37</td>
<td align="right">40437</td>
</tr>
<tr>
<td align="right">47</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n228-k23.vrp">X/X-n228-k23</a></td>
<td align="right">228</td>
<td align="right">154</td>
<td align="right">25742</td>
</tr>
<tr>
<td align="right">48</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n233-k16.vrp">X/X-n233-k16</a></td>
<td align="right">233</td>
<td align="right">631</td>
<td align="right">19230</td>
</tr>
<tr>
<td align="right">49</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n237-k14.vrp">X/X-n237-k14</a></td>
<td align="right">237</td>
<td align="right">18</td>
<td align="right">27042</td>
</tr>
<tr>
<td align="right">50</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/Golden/Golden_17.vrp">Golden/Golden_17</a></td>
<td align="right">241</td>
<td align="right">200</td>
<td align="right">707.756</td>
</tr>
<tr>
<td align="right">51</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n242-k48.vrp">X/X-n242-k48</a></td>
<td align="right">242</td>
<td align="right">28</td>
<td align="right">82751</td>
</tr>
<tr>
<td align="right">52</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n247-k50.vrp">X/X-n247-k50</a></td>
<td align="right">247</td>
<td align="right">134</td>
<td align="right">37274</td>
</tr>
<tr>
<td align="right">53</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n251-k28.vrp">X/X-n251-k28</a></td>
<td align="right">251</td>
<td align="right">69</td>
<td align="right">38684</td>
</tr>
<tr>
<td align="right">54</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/Golden/Golden_13.vrp">Golden/Golden_13</a></td>
<td align="right">253</td>
<td align="right">1000</td>
<td align="right">857.189</td>
</tr>
<tr>
<td align="right">55</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/Golden/Golden_9.vrp">Golden/Golden_9</a></td>
<td align="right">256</td>
<td align="right">1000</td>
<td align="right">579.702026</td>
</tr>
<tr>
<td align="right">56</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n256-k16.vrp">X/X-n256-k16</a></td>
<td align="right">256</td>
<td align="right">1225</td>
<td align="right">18839</td>
</tr>
<tr>
<td align="right">57</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n261-k13.vrp">X/X-n261-k13</a></td>
<td align="right">261</td>
<td align="right">1081</td>
<td align="right">26558</td>
</tr>
<tr>
<td align="right">58</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n266-k58.vrp">X/X-n266-k58</a></td>
<td align="right">266</td>
<td align="right">35</td>
<td align="right">75478</td>
</tr>
<tr>
<td align="right">59</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n270-k35.vrp">X/X-n270-k35</a></td>
<td align="right">270</td>
<td align="right">585</td>
<td align="right">35291</td>
</tr>
<tr>
<td align="right">60</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n275-k28.vrp">X/X-n275-k28</a></td>
<td align="right">275</td>
<td align="right">10</td>
<td align="right">21245</td>
</tr>
<tr>
<td align="right">61</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n280-k17.vrp">X/X-n280-k17</a></td>
<td align="right">280</td>
<td align="right">192</td>
<td align="right">33503</td>
</tr>
<tr>
<td align="right">62</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n284-k15.vrp">X/X-n284-k15</a></td>
<td align="right">284</td>
<td align="right">109</td>
<td align="right">20215.0</td>
</tr>
<tr>
<td align="right">63</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n289-k60.vrp">X/X-n289-k60</a></td>
<td align="right">289</td>
<td align="right">267</td>
<td align="right">95151</td>
</tr>
<tr>
<td align="right">64</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n294-k50.vrp">X/X-n294-k50</a></td>
<td align="right">294</td>
<td align="right">285</td>
<td align="right">47161</td>
</tr>
<tr>
<td align="right">65</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n298-k31.vrp">X/X-n298-k31</a></td>
<td align="right">298</td>
<td align="right">55</td>
<td align="right">34231</td>
</tr>
<tr>
<td align="right">66</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/Golden/Golden_18.vrp">Golden/Golden_18</a></td>
<td align="right">301</td>
<td align="right">200</td>
<td align="right">995.133</td>
</tr>
<tr>
<td align="right">67</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n303-k21.vrp">X/X-n303-k21</a></td>
<td align="right">303</td>
<td align="right">794</td>
<td align="right">21736</td>
</tr>
<tr>
<td align="right">68</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n308-k13.vrp">X/X-n308-k13</a></td>
<td align="right">308</td>
<td align="right">246</td>
<td align="right">25859</td>
</tr>
<tr>
<td align="right">69</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n313-k71.vrp">X/X-n313-k71</a></td>
<td align="right">313</td>
<td align="right">248</td>
<td align="right">94043</td>
</tr>
<tr>
<td align="right">70</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n317-k53.vrp">X/X-n317-k53</a></td>
<td align="right">317</td>
<td align="right">6</td>
<td align="right">78355</td>
</tr>
<tr>
<td align="right">71</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/Golden/Golden_14.vrp">Golden/Golden_14</a></td>
<td align="right">321</td>
<td align="right">1000</td>
<td align="right">1080.55</td>
</tr>
<tr>
<td align="right">72</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n322-k28.vrp">X/X-n322-k28</a></td>
<td align="right">322</td>
<td align="right">868</td>
<td align="right">29834</td>
</tr>
<tr>
<td align="right">73</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/Golden/Golden_10.vrp">Golden/Golden_10</a></td>
<td align="right">324</td>
<td align="right">1000</td>
<td align="right">735.427307</td>
</tr>
<tr>
<td align="right">74</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n327-k20.vrp">X/X-n327-k20</a></td>
<td align="right">327</td>
<td align="right">128</td>
<td align="right">27532</td>
</tr>
<tr>
<td align="right">75</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n331-k15.vrp">X/X-n331-k15</a></td>
<td align="right">331</td>
<td align="right">23</td>
<td align="right">31102</td>
</tr>
<tr>
<td align="right">76</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n336-k84.vrp">X/X-n336-k84</a></td>
<td align="right">336</td>
<td align="right">203</td>
<td align="right">139111</td>
</tr>
<tr>
<td align="right">77</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n344-k43.vrp">X/X-n344-k43</a></td>
<td align="right">344</td>
<td align="right">61</td>
<td align="right">42050</td>
</tr>
<tr>
<td align="right">78</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n351-k40.vrp">X/X-n351-k40</a></td>
<td align="right">351</td>
<td align="right">436</td>
<td align="right">25896</td>
</tr>
<tr>
<td align="right">79</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n359-k29.vrp">X/X-n359-k29</a></td>
<td align="right">359</td>
<td align="right">68</td>
<td align="right">51505</td>
</tr>
<tr>
<td align="right">80</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/Golden/Golden_19.vrp">Golden/Golden_19</a></td>
<td align="right">361</td>
<td align="right">200</td>
<td align="right">1365.6</td>
</tr>
<tr>
<td align="right">81</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n367-k17.vrp">X/X-n367-k17</a></td>
<td align="right">367</td>
<td align="right">218</td>
<td align="right">22814</td>
</tr>
<tr>
<td align="right">82</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n376-k94.vrp">X/X-n376-k94</a></td>
<td align="right">376</td>
<td align="right">4</td>
<td align="right">147713</td>
</tr>
<tr>
<td align="right">83</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n384-k52.vrp">X/X-n384-k52</a></td>
<td align="right">384</td>
<td align="right">564</td>
<td align="right">65928</td>
</tr>
<tr>
<td align="right">84</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n393-k38.vrp">X/X-n393-k38</a></td>
<td align="right">393</td>
<td align="right">78</td>
<td align="right">38260</td>
</tr>
<tr>
<td align="right">85</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/Golden/Golden_15.vrp">Golden/Golden_15</a></td>
<td align="right">397</td>
<td align="right">1000</td>
<td align="right">1337.2677</td>
</tr>
<tr>
<td align="right">86</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/Golden/Golden_11.vrp">Golden/Golden_11</a></td>
<td align="right">400</td>
<td align="right">1000</td>
<td align="right">911.980164</td>
</tr>
<tr>
<td align="right">87</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n401-k29.vrp">X/X-n401-k29</a></td>
<td align="right">401</td>
<td align="right">745</td>
<td align="right">66154</td>
</tr>
<tr>
<td align="right">88</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n411-k19.vrp">X/X-n411-k19</a></td>
<td align="right">411</td>
<td align="right">216</td>
<td align="right">19712</td>
</tr>
<tr>
<td align="right">89</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n420-k130.vrp">X/X-n420-k130</a></td>
<td align="right">420</td>
<td align="right">18</td>
<td align="right">107798</td>
</tr>
<tr>
<td align="right">90</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/Golden/Golden_20.vrp">Golden/Golden_20</a></td>
<td align="right">421</td>
<td align="right">200</td>
<td align="right">1817.59</td>
</tr>
<tr>
<td align="right">91</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n429-k61.vrp">X/X-n429-k61</a></td>
<td align="right">429</td>
<td align="right">536</td>
<td align="right">65449</td>
</tr>
<tr>
<td align="right">92</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n439-k37.vrp">X/X-n439-k37</a></td>
<td align="right">439</td>
<td align="right">12</td>
<td align="right">36391</td>
</tr>
<tr>
<td align="right">93</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n449-k29.vrp">X/X-n449-k29</a></td>
<td align="right">449</td>
<td align="right">777</td>
<td align="right">55233</td>
</tr>
<tr>
<td align="right">94</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n459-k26.vrp">X/X-n459-k26</a></td>
<td align="right">459</td>
<td align="right">1106</td>
<td align="right">24139</td>
</tr>
<tr>
<td align="right">95</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n469-k138.vrp">X/X-n469-k138</a></td>
<td align="right">469</td>
<td align="right">256</td>
<td align="right">221824</td>
</tr>
<tr>
<td align="right">96</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n480-k70.vrp">X/X-n480-k70</a></td>
<td align="right">480</td>
<td align="right">52</td>
<td align="right">89449</td>
</tr>
<tr>
<td align="right">97</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/Golden/Golden_16.vrp">Golden/Golden_16</a></td>
<td align="right">481</td>
<td align="right">1000</td>
<td align="right">1611.2769688292835</td>
</tr>
<tr>
<td align="right">98</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/Golden/Golden_12.vrp">Golden/Golden_12</a></td>
<td align="right">484</td>
<td align="right">1000</td>
<td align="right">1100.665283</td>
</tr>
<tr>
<td align="right">99</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n491-k59.vrp">X/X-n491-k59</a></td>
<td align="right">491</td>
<td align="right">428</td>
<td align="right">66483</td>
</tr>
<tr>
<td align="right">100</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML500_1173_01.vrp">XML500_1173_01</a></td>
<td align="right">501</td>
<td align="right">152</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">101</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML500_1176_01.vrp">XML500_1176_01</a></td>
<td align="right">501</td>
<td align="right">247</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">102</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML500_2173_01.vrp">XML500_2173_01</a></td>
<td align="right">501</td>
<td align="right">149</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">103</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML500_2176_01.vrp">XML500_2176_01</a></td>
<td align="right">501</td>
<td align="right">248</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">104</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n502-k39.vrp">X/X-n502-k39</a></td>
<td align="right">502</td>
<td align="right">13</td>
<td align="right">69226</td>
</tr>
<tr>
<td align="right">105</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n513-k21.vrp">X/X-n513-k21</a></td>
<td align="right">513</td>
<td align="right">142</td>
<td align="right">24201</td>
</tr>
<tr>
<td align="right">106</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n524-k153.vrp">X/X-n524-k153</a></td>
<td align="right">524</td>
<td align="right">125</td>
<td align="right">154593</td>
</tr>
<tr>
<td align="right">107</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n536-k96.vrp">X/X-n536-k96</a></td>
<td align="right">536</td>
<td align="right">371</td>
<td align="right">94846</td>
</tr>
<tr>
<td align="right">108</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n548-k50.vrp">X/X-n548-k50</a></td>
<td align="right">548</td>
<td align="right">11</td>
<td align="right">86700</td>
</tr>
<tr>
<td align="right">109</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n561-k42.vrp">X/X-n561-k42</a></td>
<td align="right">561</td>
<td align="right">74</td>
<td align="right">42717</td>
</tr>
<tr>
<td align="right">110</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n573-k30.vrp">X/X-n573-k30</a></td>
<td align="right">573</td>
<td align="right">210</td>
<td align="right">50673</td>
</tr>
<tr>
<td align="right">111</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n586-k159.vrp">X/X-n586-k159</a></td>
<td align="right">586</td>
<td align="right">28</td>
<td align="right">190316</td>
</tr>
<tr>
<td align="right">112</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n599-k92.vrp">X/X-n599-k92</a></td>
<td align="right">599</td>
<td align="right">487</td>
<td align="right">108451</td>
</tr>
<tr>
<td align="right">113</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n613-k62.vrp">X/X-n613-k62</a></td>
<td align="right">613</td>
<td align="right">523</td>
<td align="right">59535</td>
</tr>
<tr>
<td align="right">114</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n627-k43.vrp">X/X-n627-k43</a></td>
<td align="right">627</td>
<td align="right">110</td>
<td align="right">62164</td>
</tr>
<tr>
<td align="right">115</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n641-k35.vrp">X/X-n641-k35</a></td>
<td align="right">641</td>
<td align="right">1381</td>
<td align="right">63682</td>
</tr>
<tr>
<td align="right">116</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n655-k131.vrp">X/X-n655-k131</a></td>
<td align="right">655</td>
<td align="right">5</td>
<td align="right">106780</td>
</tr>
<tr>
<td align="right">117</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n670-k130.vrp">X/X-n670-k130</a></td>
<td align="right">670</td>
<td align="right">129</td>
<td align="right">146332</td>
</tr>
<tr>
<td align="right">118</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n685-k75.vrp">X/X-n685-k75</a></td>
<td align="right">685</td>
<td align="right">408</td>
<td align="right">68205</td>
</tr>
<tr>
<td align="right">119</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n701-k44.vrp">X/X-n701-k44</a></td>
<td align="right">701</td>
<td align="right">87</td>
<td align="right">81923</td>
</tr>
<tr>
<td align="right">120</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n716-k35.vrp">X/X-n716-k35</a></td>
<td align="right">716</td>
<td align="right">1007</td>
<td align="right">43373</td>
</tr>
<tr>
<td align="right">121</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n733-k159.vrp">X/X-n733-k159</a></td>
<td align="right">733</td>
<td align="right">25</td>
<td align="right">136187</td>
</tr>
<tr>
<td align="right">122</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n749-k98.vrp">X/X-n749-k98</a></td>
<td align="right">749</td>
<td align="right">396</td>
<td align="right">77269</td>
</tr>
<tr>
<td align="right">123</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n766-k71.vrp">X/X-n766-k71</a></td>
<td align="right">766</td>
<td align="right">166</td>
<td align="right">114417</td>
</tr>
<tr>
<td align="right">124</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n783-k48.vrp">X/X-n783-k48</a></td>
<td align="right">783</td>
<td align="right">832</td>
<td align="right">72386</td>
</tr>
<tr>
<td align="right">125</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n801-k40.vrp">X/X-n801-k40</a></td>
<td align="right">801</td>
<td align="right">20</td>
<td align="right">73305</td>
</tr>
<tr>
<td align="right">126</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n819-k171.vrp">X/X-n819-k171</a></td>
<td align="right">819</td>
<td align="right">358</td>
<td align="right">158121</td>
</tr>
<tr>
<td align="right">127</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n837-k142.vrp">X/X-n837-k142</a></td>
<td align="right">837</td>
<td align="right">44</td>
<td align="right">193737</td>
</tr>
<tr>
<td align="right">128</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n856-k95.vrp">X/X-n856-k95</a></td>
<td align="right">856</td>
<td align="right">9</td>
<td align="right">88965</td>
</tr>
<tr>
<td align="right">129</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n876-k59.vrp">X/X-n876-k59</a></td>
<td align="right">876</td>
<td align="right">764</td>
<td align="right">99299</td>
</tr>
<tr>
<td align="right">130</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n895-k37.vrp">X/X-n895-k37</a></td>
<td align="right">895</td>
<td align="right">1816</td>
<td align="right">53860</td>
</tr>
<tr>
<td align="right">131</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n916-k207.vrp">X/X-n916-k207</a></td>
<td align="right">916</td>
<td align="right">33</td>
<td align="right">329179</td>
</tr>
<tr>
<td align="right">132</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n936-k151.vrp">X/X-n936-k151</a></td>
<td align="right">936</td>
<td align="right">138</td>
<td align="right">132715</td>
</tr>
<tr>
<td align="right">133</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n957-k87.vrp">X/X-n957-k87</a></td>
<td align="right">957</td>
<td align="right">11</td>
<td align="right">85465</td>
</tr>
<tr>
<td align="right">134</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n979-k58.vrp">X/X-n979-k58</a></td>
<td align="right">979</td>
<td align="right">998</td>
<td align="right">118976</td>
</tr>
<tr>
<td align="right">135</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/X/X-n1001-k43.vrp">X/X-n1001-k43</a></td>
<td align="right">1001</td>
<td align="right">131</td>
<td align="right">72355</td>
</tr>
<tr>
<td align="right">136</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML1000_1123_01.vrp">XML1000_1123_01</a></td>
<td align="right">1001</td>
<td align="right">46</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">137</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML1000_1173_01.vrp">XML1000_1173_01</a></td>
<td align="right">1001</td>
<td align="right">152</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">138</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML1000_1176_01.vrp">XML1000_1176_01</a></td>
<td align="right">1001</td>
<td align="right">251</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">139</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML1000_2113_01.vrp">XML1000_2113_01</a></td>
<td align="right">1001</td>
<td align="right">8</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">140</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML1000_2121_01.vrp">XML1000_2121_01</a></td>
<td align="right">1001</td>
<td align="right">18</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">141</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML1000_2122_01.vrp">XML1000_2122_01</a></td>
<td align="right">1001</td>
<td align="right">29</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">142</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML1000_2123_01.vrp">XML1000_2123_01</a></td>
<td align="right">1001</td>
<td align="right">46</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">143</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML1000_2124_01.vrp">XML1000_2124_01</a></td>
<td align="right">1001</td>
<td align="right">68</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">144</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML1000_2125_01.vrp">XML1000_2125_01</a></td>
<td align="right">1001</td>
<td align="right">92</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">145</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML1000_2126_01.vrp">XML1000_2126_01</a></td>
<td align="right">1001</td>
<td align="right">145</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">146</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML1000_2133_01.vrp">XML1000_2133_01</a></td>
<td align="right">1001</td>
<td align="right">62</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">147</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML1000_2143_01.vrp">XML1000_2143_01</a></td>
<td align="right">1001</td>
<td align="right">418</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">148</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML1000_2153_01.vrp">XML1000_2153_01</a></td>
<td align="right">1001</td>
<td align="right">614</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">149</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML1000_2163_01.vrp">XML1000_2163_01</a></td>
<td align="right">1001</td>
<td align="right">414</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">150</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML1000_2173_01.vrp">XML1000_2173_01</a></td>
<td align="right">1001</td>
<td align="right">149</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">151</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML1000_2176_01.vrp">XML1000_2176_01</a></td>
<td align="right">1001</td>
<td align="right">247</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">152</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML1000_2223_01.vrp">XML1000_2223_01</a></td>
<td align="right">1001</td>
<td align="right">45</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">153</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML1000_2323_01.vrp">XML1000_2323_01</a></td>
<td align="right">1001</td>
<td align="right">46</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">154</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML1000_3123_01.vrp">XML1000_3123_01</a></td>
<td align="right">1001</td>
<td align="right">46</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">155</td>
<td align="center" rowspan="35">$\color{purple}{\textsf{M}}$</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/AGS/Leuven1.vrp">AGS/Leuven1</a></td>
<td align="right">3001</td>
<td align="right">25</td>
<td align="right">192848</td>
</tr>
<tr>
<td align="right">156</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/AGS/Leuven2.vrp">AGS/Leuven2</a></td>
<td align="right">4001</td>
<td align="right">150</td>
<td align="right">111391</td>
</tr>
<tr>
<td align="right">157</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML5000_1173_01.vrp">XML5000_1173_01</a></td>
<td align="right">5001</td>
<td align="right">151</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">158</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML5000_1176_01.vrp">XML5000_1176_01</a></td>
<td align="right">5001</td>
<td align="right">247</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">159</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML5000_2123_01.vrp">XML5000_2123_01</a></td>
<td align="right">5001</td>
<td align="right">45</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">160</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML5000_2126_01.vrp">XML5000_2126_01</a></td>
<td align="right">5001</td>
<td align="right">141</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">161</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML5000_2173_01.vrp">XML5000_2173_01</a></td>
<td align="right">5001</td>
<td align="right">149</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">162</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML5000_2176_01.vrp">XML5000_2176_01</a></td>
<td align="right">5001</td>
<td align="right">246</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">163</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML5000_2323_01.vrp">XML5000_2323_01</a></td>
<td align="right">5001</td>
<td align="right">46</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">164</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML5000_2326_01.vrp">XML5000_2326_01</a></td>
<td align="right">5001</td>
<td align="right">144</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">165</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/AGS/Antwerp1.vrp">AGS/Antwerp1</a></td>
<td align="right">6001</td>
<td align="right">30</td>
<td align="right">477277</td>
</tr>
<tr>
<td align="right">166</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/AGS/Antwerp2.vrp">AGS/Antwerp2</a></td>
<td align="right">7001</td>
<td align="right">100</td>
<td align="right">291350</td>
</tr>
<tr>
<td align="right">167</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/AGS/Ghent1.vrp">AGS/Ghent1</a></td>
<td align="right">10001</td>
<td align="right">35</td>
<td align="right">469531</td>
</tr>
<tr>
<td align="right">168</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML10000_1123_01.vrp">XML10000_1123_01</a></td>
<td align="right">10001</td>
<td align="right">45</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">169</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML10000_1173_01.vrp">XML10000_1173_01</a></td>
<td align="right">10001</td>
<td align="right">148</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">170</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML10000_1176_01.vrp">XML10000_1176_01</a></td>
<td align="right">10001</td>
<td align="right">245</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">171</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML10000_2113_01.vrp">XML10000_2113_01</a></td>
<td align="right">10001</td>
<td align="right">8</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">172</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML10000_2121_01.vrp">XML10000_2121_01</a></td>
<td align="right">10001</td>
<td align="right">17</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">173</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML10000_2122_01.vrp">XML10000_2122_01</a></td>
<td align="right">10001</td>
<td align="right">28</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">174</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML10000_2123_01.vrp">XML10000_2123_01</a></td>
<td align="right">10001</td>
<td align="right">45</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">175</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML10000_2124_01.vrp">XML10000_2124_01</a></td>
<td align="right">10001</td>
<td align="right">66</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">176</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML10000_2125_01.vrp">XML10000_2125_01</a></td>
<td align="right">10001</td>
<td align="right">89</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">177</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML10000_2126_01.vrp">XML10000_2126_01</a></td>
<td align="right">10001</td>
<td align="right">141</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">178</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML10000_2133_01.vrp">XML10000_2133_01</a></td>
<td align="right">10001</td>
<td align="right">61</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">179</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML10000_2143_01.vrp">XML10000_2143_01</a></td>
<td align="right">10001</td>
<td align="right">406</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">180</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML10000_2153_01.vrp">XML10000_2153_01</a></td>
<td align="right">10001</td>
<td align="right">608</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">181</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML10000_2163_01.vrp">XML10000_2163_01</a></td>
<td align="right">10001</td>
<td align="right">409</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">182</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML10000_2173_01.vrp">XML10000_2173_01</a></td>
<td align="right">10001</td>
<td align="right">148</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">183</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML10000_2176_01.vrp">XML10000_2176_01</a></td>
<td align="right">10001</td>
<td align="right">245</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">184</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML10000_2223_01.vrp">XML10000_2223_01</a></td>
<td align="right">10001</td>
<td align="right">45</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">185</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML10000_2323_01.vrp">XML10000_2323_01</a></td>
<td align="right">10001</td>
<td align="right">45</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">186</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML10000_3123_01.vrp">XML10000_3123_01</a></td>
<td align="right">10001</td>
<td align="right">45</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">187</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML10000_3124_01.vrp">XML10000_3124_01</a></td>
<td align="right">10001</td>
<td align="right">67</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">188</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML10000_3126_01.vrp">XML10000_3126_01</a></td>
<td align="right">10001</td>
<td align="right">141</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">189</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML10000_3146_01.vrp">XML10000_3146_01</a></td>
<td align="right">10001</td>
<td align="right">1294</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">190</td>
<td align="center" rowspan="23">$\color{orange}{\textsf{L}}$</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/AGS/Ghent2.vrp">AGS/Ghent2</a></td>
<td align="right">11001</td>
<td align="right">170</td>
<td align="right">257748</td>
</tr>
<tr>
<td align="right">191</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/AGS/Brussels1.vrp">AGS/Brussels1</a></td>
<td align="right">15001</td>
<td align="right">50</td>
<td align="right">501719</td>
</tr>
<tr>
<td align="right">192</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/AGS/Brussels2.vrp">AGS/Brussels2</a></td>
<td align="right">16001</td>
<td align="right">150</td>
<td align="right">345468</td>
</tr>
<tr>
<td align="right">193</td>
<td>FILO2</td>
<td><a href="FILO2/I/Valle-D-Aosta.vrp">I/Valle-D-Aosta</a></td>
<td align="right">20000</td>
<td align="right">50</td>
<td align="right">21679514</td>
</tr>
<tr>
<td align="right">194</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/AGS/Flanders1.vrp">AGS/Flanders1</a></td>
<td align="right">20001</td>
<td align="right">50</td>
<td align="right">7240118</td>
</tr>
<tr>
<td align="right">195</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML20000_2123_01.vrp">XML20000_2123_01</a></td>
<td align="right">20001</td>
<td align="right">45</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">196</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML20000_2126_01.vrp">XML20000_2126_01</a></td>
<td align="right">20001</td>
<td align="right">142</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">197</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML20000_3123_01.vrp">XML20000_3123_01</a></td>
<td align="right">20001</td>
<td align="right">45</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">198</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML20000_3126_01.vrp">XML20000_3126_01</a></td>
<td align="right">20001</td>
<td align="right">142</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">199</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML25000_1173_01.vrp">XML25000_1173_01</a></td>
<td align="right">25001</td>
<td align="right">150</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">200</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML25000_1176_01.vrp">XML25000_1176_01</a></td>
<td align="right">25001</td>
<td align="right">247</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">201</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML25000_2173_01.vrp">XML25000_2173_01</a></td>
<td align="right">25001</td>
<td align="right">149</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">202</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML25000_2176_01.vrp">XML25000_2176_01</a></td>
<td align="right">25001</td>
<td align="right">245</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">203</td>
<td>CVRPLIB</td>
<td><a href="CVRPLIB/AGS/Flanders2.vrp">AGS/Flanders2</a></td>
<td align="right">30001</td>
<td align="right">200</td>
<td align="right">4373244</td>
</tr>
<tr>
<td align="right">204</td>
<td>FILO2</td>
<td><a href="FILO2/I/Molise.vrp">I/Molise</a></td>
<td align="right">50000</td>
<td align="right">50</td>
<td align="right">111184982</td>
</tr>
<tr>
<td align="right">205</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML50000_1173_01.vrp">XML50000_1173_01</a></td>
<td align="right">50001</td>
<td align="right">150</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">206</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML50000_1176_01.vrp">XML50000_1176_01</a></td>
<td align="right">50001</td>
<td align="right">247</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">207</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML50000_2123_01.vrp">XML50000_2123_01</a></td>
<td align="right">50001</td>
<td align="right">45</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">208</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML50000_2126_01.vrp">XML50000_2126_01</a></td>
<td align="right">50001</td>
<td align="right">142</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">209</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML50000_2173_01.vrp">XML50000_2173_01</a></td>
<td align="right">50001</td>
<td align="right">149</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">210</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML50000_2176_01.vrp">XML50000_2176_01</a></td>
<td align="right">50001</td>
<td align="right">247</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">211</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML50000_3123_01.vrp">XML50000_3123_01</a></td>
<td align="right">50001</td>
<td align="right">45</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">212</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML50000_3126_01.vrp">XML50000_3126_01</a></td>
<td align="right">50001</td>
<td align="right">142</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">213</td>
<td align="center" rowspan="37">$\color{red}{\textsf{XL}}$</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML60000_1123_01.vrp">XML60000_1123_01</a></td>
<td align="right">60001</td>
<td align="right">45</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">214</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML60000_1126_01.vrp">XML60000_1126_01</a></td>
<td align="right">60001</td>
<td align="right">143</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">215</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML60000_2123_01.vrp">XML60000_2123_01</a></td>
<td align="right">60001</td>
<td align="right">45</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">216</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML60000_2126_01.vrp">XML60000_2126_01</a></td>
<td align="right">60001</td>
<td align="right">143</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">217</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML60000_3123_01.vrp">XML60000_3123_01</a></td>
<td align="right">60001</td>
<td align="right">45</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">218</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML60000_3126_01.vrp">XML60000_3126_01</a></td>
<td align="right">60001</td>
<td align="right">143</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">219</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML75000_1173_01.vrp">XML75000_1173_01</a></td>
<td align="right">75001</td>
<td align="right">149</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">220</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML75000_1176_01.vrp">XML75000_1176_01</a></td>
<td align="right">75001</td>
<td align="right">247</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">221</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML75000_2173_01.vrp">XML75000_2173_01</a></td>
<td align="right">75001</td>
<td align="right">149</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">222</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML75000_2176_01.vrp">XML75000_2176_01</a></td>
<td align="right">75001</td>
<td align="right">247</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">223</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML80000_1123_01.vrp">XML80000_1123_01</a></td>
<td align="right">80001</td>
<td align="right">45</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">224</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML80000_1126_01.vrp">XML80000_1126_01</a></td>
<td align="right">80001</td>
<td align="right">142</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">225</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML80000_2123_01.vrp">XML80000_2123_01</a></td>
<td align="right">80001</td>
<td align="right">45</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">226</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML80000_2126_01.vrp">XML80000_2126_01</a></td>
<td align="right">80001</td>
<td align="right">142</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">227</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML80000_3123_01.vrp">XML80000_3123_01</a></td>
<td align="right">80001</td>
<td align="right">45</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">228</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML80000_3126_01.vrp">XML80000_3126_01</a></td>
<td align="right">80001</td>
<td align="right">142</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">229</td>
<td>FILO2</td>
<td><a href="FILO2/I/Trentino-Alto-Adige.vrp">I/Trentino-Alto-Adige</a></td>
<td align="right">100000</td>
<td align="right">150</td>
<td align="right">102063181</td>
</tr>
<tr>
<td align="right">230</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML100000_1123_01.vrp">XML100000_1123_01</a></td>
<td align="right">100001</td>
<td align="right">45</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">231</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML100000_1173_01.vrp">XML100000_1173_01</a></td>
<td align="right">100001</td>
<td align="right">149</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">232</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML100000_1176_01.vrp">XML100000_1176_01</a></td>
<td align="right">100001</td>
<td align="right">247</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">233</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML100000_2113_01.vrp">XML100000_2113_01</a></td>
<td align="right">100001</td>
<td align="right">8</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">234</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML100000_2121_01.vrp">XML100000_2121_01</a></td>
<td align="right">100001</td>
<td align="right">17</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">235</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML100000_2122_01.vrp">XML100000_2122_01</a></td>
<td align="right">100001</td>
<td align="right">29</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">236</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML100000_2123_01.vrp">XML100000_2123_01</a></td>
<td align="right">100001</td>
<td align="right">45</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">237</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML100000_2124_01.vrp">XML100000_2124_01</a></td>
<td align="right">100001</td>
<td align="right">67</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">238</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML100000_2125_01.vrp">XML100000_2125_01</a></td>
<td align="right">100001</td>
<td align="right">90</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">239</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML100000_2126_01.vrp">XML100000_2126_01</a></td>
<td align="right">100001</td>
<td align="right">143</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">240</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML100000_2133_01.vrp">XML100000_2133_01</a></td>
<td align="right">100001</td>
<td align="right">62</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">241</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML100000_2143_01.vrp">XML100000_2143_01</a></td>
<td align="right">100001</td>
<td align="right">411</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">242</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML100000_2153_01.vrp">XML100000_2153_01</a></td>
<td align="right">100001</td>
<td align="right">610</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">243</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML100000_2163_01.vrp">XML100000_2163_01</a></td>
<td align="right">100001</td>
<td align="right">410</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">244</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML100000_2173_01.vrp">XML100000_2173_01</a></td>
<td align="right">100001</td>
<td align="right">149</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">245</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML100000_2176_01.vrp">XML100000_2176_01</a></td>
<td align="right">100001</td>
<td align="right">246</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">246</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML100000_2223_01.vrp">XML100000_2223_01</a></td>
<td align="right">100001</td>
<td align="right">45</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">247</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML100000_2323_01.vrp">XML100000_2323_01</a></td>
<td align="right">100001</td>
<td align="right">45</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">248</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML100000_3123_01.vrp">XML100000_3123_01</a></td>
<td align="right">100001</td>
<td align="right">45</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">249</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML100000_3126_01.vrp">XML100000_3126_01</a></td>
<td align="right">100001</td>
<td align="right">143</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">250</td>
<td align="center" rowspan="41">$\color{teal}{\textsf{XXL}}$</td>
<td>FILO2</td>
<td><a href="FILO2/I/Basilicata.vrp">I/Basilicata</a></td>
<td align="right">150000</td>
<td align="right">150</td>
<td align="right">175623919</td>
</tr>
<tr>
<td align="right">251</td>
<td>FILO2</td>
<td><a href="FILO2/I/Umbria.vrp">I/Umbria</a></td>
<td align="right">200000</td>
<td align="right">50</td>
<td align="right">545507981</td>
</tr>
<tr>
<td align="right">252</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML200000_2123_01.vrp">XML200000_2123_01</a></td>
<td align="right">200001</td>
<td align="right">45</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">253</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML200000_2126_01.vrp">XML200000_2126_01</a></td>
<td align="right">200001</td>
<td align="right">143</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">254</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML200000_3123_01.vrp">XML200000_3123_01</a></td>
<td align="right">200001</td>
<td align="right">45</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">255</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML200000_3126_01.vrp">XML200000_3126_01</a></td>
<td align="right">200001</td>
<td align="right">143</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">256</td>
<td>FILO2</td>
<td><a href="FILO2/I/Abruzzo.vrp">I/Abruzzo</a></td>
<td align="right">250000</td>
<td align="right">200</td>
<td align="right">311712556</td>
</tr>
<tr>
<td align="right">257</td>
<td>FILO2</td>
<td><a href="FILO2/I/Friuli-Venezia-Giulia.vrp">I/Friuli-Venezia-Giulia</a></td>
<td align="right">300000</td>
<td align="right">200</td>
<td align="right">415805616</td>
</tr>
<tr>
<td align="right">258</td>
<td>FILO2</td>
<td><a href="FILO2/I/Liguria.vrp">I/Liguria</a></td>
<td align="right">320000</td>
<td align="right">50</td>
<td align="right">1426389867</td>
</tr>
<tr>
<td align="right">259</td>
<td>FILO2</td>
<td><a href="FILO2/I/Calabria.vrp">I/Calabria</a></td>
<td align="right">380000</td>
<td align="right">50</td>
<td align="right">1964651530</td>
</tr>
<tr>
<td align="right">260</td>
<td>FILO2</td>
<td><a href="FILO2/I/Marche.vrp">I/Marche</a></td>
<td align="right">420000</td>
<td align="right">200</td>
<td align="right">420484426</td>
</tr>
<tr>
<td align="right">261</td>
<td>FILO2</td>
<td><a href="FILO2/I/Sardegna.vrp">I/Sardegna</a></td>
<td align="right">470000</td>
<td align="right">200</td>
<td align="right">827934149</td>
</tr>
<tr>
<td align="right">262</td>
<td>FILO2</td>
<td><a href="FILO2/I/Campania.vrp">I/Campania</a></td>
<td align="right">500000</td>
<td align="right">200</td>
<td align="right">391859276</td>
</tr>
<tr>
<td align="right">263</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML500000_1173_01.vrp">XML500000_1173_01</a></td>
<td align="right">500001</td>
<td align="right">150</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">264</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML500000_1176_01.vrp">XML500000_1176_01</a></td>
<td align="right">500001</td>
<td align="right">247</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">265</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML500000_2123_01.vrp">XML500000_2123_01</a></td>
<td align="right">500001</td>
<td align="right">45</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">266</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML500000_2126_01.vrp">XML500000_2126_01</a></td>
<td align="right">500001</td>
<td align="right">143</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">267</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML500000_2173_01.vrp">XML500000_2173_01</a></td>
<td align="right">500001</td>
<td align="right">150</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">268</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML500000_2176_01.vrp">XML500000_2176_01</a></td>
<td align="right">500001</td>
<td align="right">247</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">269</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML500000_3123_01.vrp">XML500000_3123_01</a></td>
<td align="right">500001</td>
<td align="right">45</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">270</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML500000_3126_01.vrp">XML500000_3126_01</a></td>
<td align="right">500001</td>
<td align="right">143</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">271</td>
<td>FILO2</td>
<td><a href="FILO2/I/Piemonte.vrp">I/Piemonte</a></td>
<td align="right">600000</td>
<td align="right">50</td>
<td align="right">2627446164</td>
</tr>
<tr>
<td align="right">272</td>
<td>FILO2</td>
<td><a href="FILO2/I/Toscana.vrp">I/Toscana</a></td>
<td align="right">700000</td>
<td align="right">150</td>
<td align="right">1084417188</td>
</tr>
<tr>
<td align="right">273</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML700000_2123_01.vrp">XML700000_2123_01</a></td>
<td align="right">700001</td>
<td align="right">45</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">274</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML700000_2126_01.vrp">XML700000_2126_01</a></td>
<td align="right">700001</td>
<td align="right">142</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">275</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML700000_3123_01.vrp">XML700000_3123_01</a></td>
<td align="right">700001</td>
<td align="right">45</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">276</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML700000_3126_01.vrp">XML700000_3126_01</a></td>
<td align="right">700001</td>
<td align="right">142</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">277</td>
<td>FILO2</td>
<td><a href="FILO2/I/Puglia.vrp">I/Puglia</a></td>
<td align="right">750000</td>
<td align="right">200</td>
<td align="right">1464797603</td>
</tr>
<tr>
<td align="right">278</td>
<td>FILO2</td>
<td><a href="FILO2/I/Sicilia.vrp">I/Sicilia</a></td>
<td align="right">800000</td>
<td align="right">200</td>
<td align="right">1774262462</td>
</tr>
<tr>
<td align="right">279</td>
<td>FILO2</td>
<td><a href="FILO2/I/Veneto.vrp">I/Veneto</a></td>
<td align="right">850000</td>
<td align="right">200</td>
<td align="right">1050488613</td>
</tr>
<tr>
<td align="right">280</td>
<td>FILO2</td>
<td><a href="FILO2/I/Emilia-Romagna.vrp">I/Emilia-Romagna</a></td>
<td align="right">900000</td>
<td align="right">50</td>
<td align="right">5405446715</td>
</tr>
<tr>
<td align="right">281</td>
<td>FILO2</td>
<td><a href="FILO2/I/Lombardia.vrp">I/Lombardia</a></td>
<td align="right">950000</td>
<td align="right">150</td>
<td align="right">1339900081</td>
</tr>
<tr>
<td align="right">282</td>
<td>FILO2</td>
<td><a href="FILO2/I/Lazio.vrp">I/Lazio</a></td>
<td align="right">1000000</td>
<td align="right">50</td>
<td align="right">3145381332</td>
</tr>
<tr>
<td align="right">283</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML1000000_1173_01.vrp">XML1000000_1173_01</a></td>
<td align="right">1000001</td>
<td align="right">150</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">284</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML1000000_1176_01.vrp">XML1000000_1176_01</a></td>
<td align="right">1000001</td>
<td align="right">247</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">285</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML1000000_2123_01.vrp">XML1000000_2123_01</a></td>
<td align="right">1000001</td>
<td align="right">45</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">286</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML1000000_2126_01.vrp">XML1000000_2126_01</a></td>
<td align="right">1000001</td>
<td align="right">142</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">287</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML1000000_2173_01.vrp">XML1000000_2173_01</a></td>
<td align="right">1000001</td>
<td align="right">150</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">288</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML1000000_2176_01.vrp">XML1000000_2176_01</a></td>
<td align="right">1000001</td>
<td align="right">247</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">289</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML1000000_3123_01.vrp">XML1000000_3123_01</a></td>
<td align="right">1000001</td>
<td align="right">45</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">290</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML1000000_3126_01.vrp">XML1000000_3126_01</a></td>
<td align="right">1000001</td>
<td align="right">142</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">291</td>
<td align="center" rowspan="30">$\color{magenta}{\textsf{XXXL}}$</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML1500000_1173_01.vrp">XML1500000_1173_01</a></td>
<td align="right">1500001</td>
<td align="right">149</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">292</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML1500000_1176_01.vrp">XML1500000_1176_01</a></td>
<td align="right">1500001</td>
<td align="right">247</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">293</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML2000000_1113_01.vrp">XML2000000_1113_01</a></td>
<td align="right">2000001</td>
<td align="right">8</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">294</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML2000000_1121_01.vrp">XML2000000_1121_01</a></td>
<td align="right">2000001</td>
<td align="right">17</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">295</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML2000000_1123_01.vrp">XML2000000_1123_01</a></td>
<td align="right">2000001</td>
<td align="right">45</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">296</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML2000000_1126_01.vrp">XML2000000_1126_01</a></td>
<td align="right">2000001</td>
<td align="right">142</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">297</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML2000000_1173_01.vrp">XML2000000_1173_01</a></td>
<td align="right">2000001</td>
<td align="right">149</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">298</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML2000000_1176_01.vrp">XML2000000_1176_01</a></td>
<td align="right">2000001</td>
<td align="right">247</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">299</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML2000000_2113_01.vrp">XML2000000_2113_01</a></td>
<td align="right">2000001</td>
<td align="right">8</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">300</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML2000000_2121_01.vrp">XML2000000_2121_01</a></td>
<td align="right">2000001</td>
<td align="right">17</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">301</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML2000000_2122_01.vrp">XML2000000_2122_01</a></td>
<td align="right">2000001</td>
<td align="right">29</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">302</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML2000000_2123_01.vrp">XML2000000_2123_01</a></td>
<td align="right">2000001</td>
<td align="right">45</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">303</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML2000000_2124_01.vrp">XML2000000_2124_01</a></td>
<td align="right">2000001</td>
<td align="right">67</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">304</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML2000000_2125_01.vrp">XML2000000_2125_01</a></td>
<td align="right">2000001</td>
<td align="right">90</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">305</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML2000000_2126_01.vrp">XML2000000_2126_01</a></td>
<td align="right">2000001</td>
<td align="right">142</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">306</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML2000000_2133_01.vrp">XML2000000_2133_01</a></td>
<td align="right">2000001</td>
<td align="right">61</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">307</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML2000000_2143_01.vrp">XML2000000_2143_01</a></td>
<td align="right">2000001</td>
<td align="right">411</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">308</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML2000000_2153_01.vrp">XML2000000_2153_01</a></td>
<td align="right">2000001</td>
<td align="right">610</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">309</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML2000000_2163_01.vrp">XML2000000_2163_01</a></td>
<td align="right">2000001</td>
<td align="right">411</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">310</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML2000000_2173_01.vrp">XML2000000_2173_01</a></td>
<td align="right">2000001</td>
<td align="right">149</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">311</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML2000000_2176_01.vrp">XML2000000_2176_01</a></td>
<td align="right">2000001</td>
<td align="right">247</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">312</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML2000000_2223_01.vrp">XML2000000_2223_01</a></td>
<td align="right">2000001</td>
<td align="right">45</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">313</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML2000000_2323_01.vrp">XML2000000_2323_01</a></td>
<td align="right">2000001</td>
<td align="right">45</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">314</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML2000000_3113_01.vrp">XML2000000_3113_01</a></td>
<td align="right">2000001</td>
<td align="right">8</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">315</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML2000000_3121_01.vrp">XML2000000_3121_01</a></td>
<td align="right">2000001</td>
<td align="right">17</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">316</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML2000000_3123_01.vrp">XML2000000_3123_01</a></td>
<td align="right">2000001</td>
<td align="right">45</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">317</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML2000000_3126_01.vrp">XML2000000_3126_01</a></td>
<td align="right">2000001</td>
<td align="right">142</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">318</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML2000000_3161_01.vrp">XML2000000_3161_01</a></td>
<td align="right">2000001</td>
<td align="right">155</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">319</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML2000000_3173_01.vrp">XML2000000_3173_01</a></td>
<td align="right">2000001</td>
<td align="right">149</td>
<td align="right">—</td>
</tr>
<tr>
<td align="right">320</td>
<td>Synthetic</td>
<td><a href="Synthetic/XML2000000_3176_01.vrp">XML2000000_3176_01</a></td>
<td align="right">2000001</td>
<td align="right">247</td>
<td align="right">—</td>
</tr>
</tbody>
</table>

---

## CVRPLIB

Standard capacity-only CVRP benchmarks from [CVRPLIB](http://vrp.atd-lab.inf.puc-rio.br/index.php/en/) *(accessed 25 July 2026)*.

- Layout: TSPLIB `.vrp` + matching BKS `.sol`
- Edge weights: `EUC_2D`
- Constraint: vehicle capacity `Q` only

| Set | # | Source |
|:---:|--:|:-------|
| **CMT** | 7 | Christofides, Mingozzi & Toth |
| **Golden** | 12 | Golden et al. (Golden_9–20) |
| **X** | 100 | Uchoa et al. |
| **AGS** | 10 | Arnold, Gendreau & Sörensen (XXL cities) |

### Exclusions

Distance- / service-constrained variants are not kept:

- `Golden_1`–`Golden_8` — `DISTANCE`
- `CMT6`–`CMT10`, `CMT13`–`CMT14` — `DISTANCE` + `SERVICE_TIME`
- **Li** set — every instance has `DISTANCE`

---

## FILO2

Large-scale Italian regional instances under `FILO2/I/`.

- Layout: TSPLIB `.vrp` (BKS costs from the paper; no `.sol` routes bundled here)
- Edge weights: `EUC_2D`
- Constraint: vehicle capacity `Q`
- Scale: **L** / **XL** / **XXL** (~20k – 1M customers)
- Count: **20** instances

**Reference:** L. Accorsi & D. Vigo, *A fast and scalable heuristic for the solution of large-scale capacitated vehicle routing problems*, Computers & Operations Research, 2024. [doi:10.1016/j.cor.2024.106562](https://dl.acm.org/doi/10.1016/j.cor.2024.106562)

---

## Synthetic

XML-style synthetic CVRP instances under `Synthetic/`, generated with the Uchoa et al. generator in `Inputs-generation/` (*Generated as the XML100 dataset from the CVRPLIB*).

- Layout: TSPLIB `.vrp` (no BKS / `.sol` bundled)
- Edge weights: `EUC_2D`
- Constraint: vehicle capacity `Q`
- Count: **171** instances
- Scale: **XS** – **XXXL** (10 – 2,000,000 customers)

### Naming

`XML<n>_<depotPos><custPos><demandType><avgRouteSize>_<instanceID>.vrp`

| Field | Values |
|:------|:-------|
| `n` | Number of customers |
| Depot positioning | `1` Random · `2` Centered · `3` Cornered |
| Customer positioning | `1` Random · `2` Clustered · `3` Random-clustered |
| Demand distribution | `1` Unitary · `2`–`5` small/large ± variance · `6` quadrant-dependent · `7` few large, many small |
| Average route size | `1` Very short · `2` Short · `3` Medium · `4` Long · `5` Very long · `6` Ultra long |
| `instanceID` | Instance index (here `01`) |

**References:** Uchoa et al. (2017), *New benchmark instances for the Capacitated Vehicle Routing Problem*, EJOR. Queiroga et al. (2022), *10,000 optimal CVRP solutions for testing machine learning based heuristics*.

---

## Sample

Tiny hand-written instances for quick local checks (not part of the benchmark counts above):

- [Sample/eg](Sample/eg.vrp) — `N=7`, `Q=5`
- [Sample/toy](Sample/toy.vrp) — `N=6`, `Q=30`
