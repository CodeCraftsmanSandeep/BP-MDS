# Input Instances

Capacity-only CVRP benchmarks from CVRPLIB, FILO2, and Synthetic XML-style instances *(CVRPLIB accessed 25 July 2026)*.

**320** instances &nbsp;·&nbsp; **CVRPLIB** 129 &nbsp;·&nbsp; **FILO2** 20 &nbsp;·&nbsp; **Synthetic** 171

Machine-readable index: [`instances.csv`](instances.csv)

---

## Instances

| Symbol | Meaning |
|:------:|:--------|
| **Size** | By **#Customers** (`N−1`): $\color{green}{\textsf{XS}}$ 1–100 · $\color{blue}{\textsf{S}}$ 101–1,000 · $\color{purple}{\textsf{M}}$ 1,001–10,000 · $\color{orange}{\textsf{L}}$ 10,001–50,000 · $\color{red}{\textsf{XL}}$ 50,001–100,000 · $\color{teal}{\textsf{XXL}}$ 100,001–1,000,000 · $\color{magenta}{\textsf{XXXL}}$ 1,000,001–10,000,000 |
| **Source** | `CVRPLIB` · `FILO2` · `Synthetic` |
| **Instance** | Clickable path under the source |
| **N** | `#Customers + 1` (= `DIMENSION`, includes depot) |
| **Q** | Vehicle capacity |
| **BKS** | Best-known solution cost (if available) |

| S.No | Size | Source | Instance | N | Q | BKS |
|----:|:----:|:-------|:---------|--:|--:|----:|
| 1 | $\color{green}{\textsf{XS}}$ | Synthetic | [XML10_1173_01](Synthetic/XML10_1173_01.vrp) | 11 | 47 | — |
| 2 | $\color{green}{\textsf{XS}}$ | Synthetic | [XML10_1176_01](Synthetic/XML10_1176_01.vrp) | 11 | 148 | — |
| 3 | $\color{green}{\textsf{XS}}$ | Synthetic | [XML10_2173_01](Synthetic/XML10_2173_01.vrp) | 11 | 45 | — |
| 4 | $\color{green}{\textsf{XS}}$ | Synthetic | [XML10_2176_01](Synthetic/XML10_2176_01.vrp) | 11 | 142 | — |
| 5 | $\color{green}{\textsf{XS}}$ | CVRPLIB | [CMT/CMT1](CVRPLIB/CMT/CMT1.vrp) | 51 | 160 | 524.611 |
| 6 | $\color{green}{\textsf{XS}}$ | Synthetic | [XML50_1173_01](Synthetic/XML50_1173_01.vrp) | 51 | 134 | — |
| 7 | $\color{green}{\textsf{XS}}$ | Synthetic | [XML50_1176_01](Synthetic/XML50_1176_01.vrp) | 51 | 182 | — |
| 8 | $\color{green}{\textsf{XS}}$ | Synthetic | [XML50_2173_01](Synthetic/XML50_2173_01.vrp) | 51 | 142 | — |
| 9 | $\color{green}{\textsf{XS}}$ | Synthetic | [XML50_2176_01](Synthetic/XML50_2176_01.vrp) | 51 | 171 | — |
| 10 | $\color{green}{\textsf{XS}}$ | CVRPLIB | [CMT/CMT2](CVRPLIB/CMT/CMT2.vrp) | 76 | 140 | 835.262 |
| 11 | $\color{green}{\textsf{XS}}$ | CVRPLIB | [CMT/CMT12](CVRPLIB/CMT/CMT12.vrp) | 101 | 200 | 819.558 |
| 12 | $\color{green}{\textsf{XS}}$ | CVRPLIB | [CMT/CMT3](CVRPLIB/CMT/CMT3.vrp) | 101 | 200 | 826.137 |
| 13 | $\color{green}{\textsf{XS}}$ | CVRPLIB | [X/X-n101-k25](CVRPLIB/X/X-n101-k25.vrp) | 101 | 206 | 27591 |
| 14 | $\color{green}{\textsf{XS}}$ | Synthetic | [XML100_1173_01](Synthetic/XML100_1173_01.vrp) | 101 | 139 | — |
| 15 | $\color{green}{\textsf{XS}}$ | Synthetic | [XML100_1176_01](Synthetic/XML100_1176_01.vrp) | 101 | 215 | — |
| 16 | $\color{green}{\textsf{XS}}$ | Synthetic | [XML100_2173_01](Synthetic/XML100_2173_01.vrp) | 101 | 138 | — |
| 17 | $\color{green}{\textsf{XS}}$ | Synthetic | [XML100_2176_01](Synthetic/XML100_2176_01.vrp) | 101 | 211 | — |
| 18 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n106-k14](CVRPLIB/X/X-n106-k14.vrp) | 106 | 600 | 26362 |
| 19 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n110-k13](CVRPLIB/X/X-n110-k13.vrp) | 110 | 66 | 14971 |
| 20 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n115-k10](CVRPLIB/X/X-n115-k10.vrp) | 115 | 169 | 12747 |
| 21 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n120-k6](CVRPLIB/X/X-n120-k6.vrp) | 120 | 21 | 13332 |
| 22 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [CMT/CMT11](CVRPLIB/CMT/CMT11.vrp) | 121 | 200 | 1042.12 |
| 23 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n125-k30](CVRPLIB/X/X-n125-k30.vrp) | 125 | 188 | 55539 |
| 24 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n129-k18](CVRPLIB/X/X-n129-k18.vrp) | 129 | 39 | 28940 |
| 25 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n134-k13](CVRPLIB/X/X-n134-k13.vrp) | 134 | 643 | 10916 |
| 26 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n139-k10](CVRPLIB/X/X-n139-k10.vrp) | 139 | 106 | 13590 |
| 27 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n143-k7](CVRPLIB/X/X-n143-k7.vrp) | 143 | 1190 | 15700 |
| 28 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n148-k46](CVRPLIB/X/X-n148-k46.vrp) | 148 | 18 | 43448 |
| 29 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [CMT/CMT4](CVRPLIB/CMT/CMT4.vrp) | 151 | 200 | 1028.42 |
| 30 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n153-k22](CVRPLIB/X/X-n153-k22.vrp) | 153 | 144 | 21220 |
| 31 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n157-k13](CVRPLIB/X/X-n157-k13.vrp) | 157 | 12 | 16876 |
| 32 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n162-k11](CVRPLIB/X/X-n162-k11.vrp) | 162 | 1174 | 14138 |
| 33 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n167-k10](CVRPLIB/X/X-n167-k10.vrp) | 167 | 133 | 20557 |
| 34 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n172-k51](CVRPLIB/X/X-n172-k51.vrp) | 172 | 161 | 45607 |
| 35 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n176-k26](CVRPLIB/X/X-n176-k26.vrp) | 176 | 142 | 47812 |
| 36 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n181-k23](CVRPLIB/X/X-n181-k23.vrp) | 181 | 8 | 25569 |
| 37 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n186-k15](CVRPLIB/X/X-n186-k15.vrp) | 186 | 974 | 24145 |
| 38 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n190-k8](CVRPLIB/X/X-n190-k8.vrp) | 190 | 138 | 16980 |
| 39 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n195-k51](CVRPLIB/X/X-n195-k51.vrp) | 195 | 181 | 44225 |
| 40 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [CMT/CMT5](CVRPLIB/CMT/CMT5.vrp) | 200 | 200 | 1291.289144 |
| 41 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n200-k36](CVRPLIB/X/X-n200-k36.vrp) | 200 | 402 | 58578 |
| 42 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n204-k19](CVRPLIB/X/X-n204-k19.vrp) | 204 | 836 | 19565 |
| 43 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n209-k16](CVRPLIB/X/X-n209-k16.vrp) | 209 | 101 | 30656 |
| 44 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n214-k11](CVRPLIB/X/X-n214-k11.vrp) | 214 | 944 | 10856 |
| 45 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n219-k73](CVRPLIB/X/X-n219-k73.vrp) | 219 | 3 | 117595 |
| 46 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n223-k34](CVRPLIB/X/X-n223-k34.vrp) | 223 | 37 | 40437 |
| 47 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n228-k23](CVRPLIB/X/X-n228-k23.vrp) | 228 | 154 | 25742 |
| 48 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n233-k16](CVRPLIB/X/X-n233-k16.vrp) | 233 | 631 | 19230 |
| 49 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n237-k14](CVRPLIB/X/X-n237-k14.vrp) | 237 | 18 | 27042 |
| 50 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [Golden/Golden_17](CVRPLIB/Golden/Golden_17.vrp) | 241 | 200 | 707.756 |
| 51 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n242-k48](CVRPLIB/X/X-n242-k48.vrp) | 242 | 28 | 82751 |
| 52 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n247-k50](CVRPLIB/X/X-n247-k50.vrp) | 247 | 134 | 37274 |
| 53 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n251-k28](CVRPLIB/X/X-n251-k28.vrp) | 251 | 69 | 38684 |
| 54 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [Golden/Golden_13](CVRPLIB/Golden/Golden_13.vrp) | 253 | 1000 | 857.189 |
| 55 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [Golden/Golden_9](CVRPLIB/Golden/Golden_9.vrp) | 256 | 1000 | 579.702026 |
| 56 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n256-k16](CVRPLIB/X/X-n256-k16.vrp) | 256 | 1225 | 18839 |
| 57 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n261-k13](CVRPLIB/X/X-n261-k13.vrp) | 261 | 1081 | 26558 |
| 58 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n266-k58](CVRPLIB/X/X-n266-k58.vrp) | 266 | 35 | 75478 |
| 59 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n270-k35](CVRPLIB/X/X-n270-k35.vrp) | 270 | 585 | 35291 |
| 60 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n275-k28](CVRPLIB/X/X-n275-k28.vrp) | 275 | 10 | 21245 |
| 61 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n280-k17](CVRPLIB/X/X-n280-k17.vrp) | 280 | 192 | 33503 |
| 62 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n284-k15](CVRPLIB/X/X-n284-k15.vrp) | 284 | 109 | 20215.0 |
| 63 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n289-k60](CVRPLIB/X/X-n289-k60.vrp) | 289 | 267 | 95151 |
| 64 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n294-k50](CVRPLIB/X/X-n294-k50.vrp) | 294 | 285 | 47161 |
| 65 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n298-k31](CVRPLIB/X/X-n298-k31.vrp) | 298 | 55 | 34231 |
| 66 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [Golden/Golden_18](CVRPLIB/Golden/Golden_18.vrp) | 301 | 200 | 995.133 |
| 67 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n303-k21](CVRPLIB/X/X-n303-k21.vrp) | 303 | 794 | 21736 |
| 68 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n308-k13](CVRPLIB/X/X-n308-k13.vrp) | 308 | 246 | 25859 |
| 69 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n313-k71](CVRPLIB/X/X-n313-k71.vrp) | 313 | 248 | 94043 |
| 70 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n317-k53](CVRPLIB/X/X-n317-k53.vrp) | 317 | 6 | 78355 |
| 71 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [Golden/Golden_14](CVRPLIB/Golden/Golden_14.vrp) | 321 | 1000 | 1080.55 |
| 72 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n322-k28](CVRPLIB/X/X-n322-k28.vrp) | 322 | 868 | 29834 |
| 73 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [Golden/Golden_10](CVRPLIB/Golden/Golden_10.vrp) | 324 | 1000 | 735.427307 |
| 74 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n327-k20](CVRPLIB/X/X-n327-k20.vrp) | 327 | 128 | 27532 |
| 75 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n331-k15](CVRPLIB/X/X-n331-k15.vrp) | 331 | 23 | 31102 |
| 76 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n336-k84](CVRPLIB/X/X-n336-k84.vrp) | 336 | 203 | 139111 |
| 77 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n344-k43](CVRPLIB/X/X-n344-k43.vrp) | 344 | 61 | 42050 |
| 78 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n351-k40](CVRPLIB/X/X-n351-k40.vrp) | 351 | 436 | 25896 |
| 79 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n359-k29](CVRPLIB/X/X-n359-k29.vrp) | 359 | 68 | 51505 |
| 80 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [Golden/Golden_19](CVRPLIB/Golden/Golden_19.vrp) | 361 | 200 | 1365.6 |
| 81 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n367-k17](CVRPLIB/X/X-n367-k17.vrp) | 367 | 218 | 22814 |
| 82 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n376-k94](CVRPLIB/X/X-n376-k94.vrp) | 376 | 4 | 147713 |
| 83 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n384-k52](CVRPLIB/X/X-n384-k52.vrp) | 384 | 564 | 65928 |
| 84 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n393-k38](CVRPLIB/X/X-n393-k38.vrp) | 393 | 78 | 38260 |
| 85 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [Golden/Golden_15](CVRPLIB/Golden/Golden_15.vrp) | 397 | 1000 | 1337.2677 |
| 86 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [Golden/Golden_11](CVRPLIB/Golden/Golden_11.vrp) | 400 | 1000 | 911.980164 |
| 87 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n401-k29](CVRPLIB/X/X-n401-k29.vrp) | 401 | 745 | 66154 |
| 88 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n411-k19](CVRPLIB/X/X-n411-k19.vrp) | 411 | 216 | 19712 |
| 89 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n420-k130](CVRPLIB/X/X-n420-k130.vrp) | 420 | 18 | 107798 |
| 90 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [Golden/Golden_20](CVRPLIB/Golden/Golden_20.vrp) | 421 | 200 | 1817.59 |
| 91 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n429-k61](CVRPLIB/X/X-n429-k61.vrp) | 429 | 536 | 65449 |
| 92 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n439-k37](CVRPLIB/X/X-n439-k37.vrp) | 439 | 12 | 36391 |
| 93 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n449-k29](CVRPLIB/X/X-n449-k29.vrp) | 449 | 777 | 55233 |
| 94 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n459-k26](CVRPLIB/X/X-n459-k26.vrp) | 459 | 1106 | 24139 |
| 95 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n469-k138](CVRPLIB/X/X-n469-k138.vrp) | 469 | 256 | 221824 |
| 96 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n480-k70](CVRPLIB/X/X-n480-k70.vrp) | 480 | 52 | 89449 |
| 97 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [Golden/Golden_16](CVRPLIB/Golden/Golden_16.vrp) | 481 | 1000 | 1611.2769688292835 |
| 98 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [Golden/Golden_12](CVRPLIB/Golden/Golden_12.vrp) | 484 | 1000 | 1100.665283 |
| 99 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n491-k59](CVRPLIB/X/X-n491-k59.vrp) | 491 | 428 | 66483 |
| 100 | $\color{blue}{\textsf{S}}$ | Synthetic | [XML500_1173_01](Synthetic/XML500_1173_01.vrp) | 501 | 152 | — |
| 101 | $\color{blue}{\textsf{S}}$ | Synthetic | [XML500_1176_01](Synthetic/XML500_1176_01.vrp) | 501 | 247 | — |
| 102 | $\color{blue}{\textsf{S}}$ | Synthetic | [XML500_2173_01](Synthetic/XML500_2173_01.vrp) | 501 | 149 | — |
| 103 | $\color{blue}{\textsf{S}}$ | Synthetic | [XML500_2176_01](Synthetic/XML500_2176_01.vrp) | 501 | 248 | — |
| 104 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n502-k39](CVRPLIB/X/X-n502-k39.vrp) | 502 | 13 | 69226 |
| 105 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n513-k21](CVRPLIB/X/X-n513-k21.vrp) | 513 | 142 | 24201 |
| 106 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n524-k153](CVRPLIB/X/X-n524-k153.vrp) | 524 | 125 | 154593 |
| 107 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n536-k96](CVRPLIB/X/X-n536-k96.vrp) | 536 | 371 | 94846 |
| 108 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n548-k50](CVRPLIB/X/X-n548-k50.vrp) | 548 | 11 | 86700 |
| 109 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n561-k42](CVRPLIB/X/X-n561-k42.vrp) | 561 | 74 | 42717 |
| 110 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n573-k30](CVRPLIB/X/X-n573-k30.vrp) | 573 | 210 | 50673 |
| 111 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n586-k159](CVRPLIB/X/X-n586-k159.vrp) | 586 | 28 | 190316 |
| 112 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n599-k92](CVRPLIB/X/X-n599-k92.vrp) | 599 | 487 | 108451 |
| 113 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n613-k62](CVRPLIB/X/X-n613-k62.vrp) | 613 | 523 | 59535 |
| 114 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n627-k43](CVRPLIB/X/X-n627-k43.vrp) | 627 | 110 | 62164 |
| 115 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n641-k35](CVRPLIB/X/X-n641-k35.vrp) | 641 | 1381 | 63682 |
| 116 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n655-k131](CVRPLIB/X/X-n655-k131.vrp) | 655 | 5 | 106780 |
| 117 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n670-k130](CVRPLIB/X/X-n670-k130.vrp) | 670 | 129 | 146332 |
| 118 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n685-k75](CVRPLIB/X/X-n685-k75.vrp) | 685 | 408 | 68205 |
| 119 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n701-k44](CVRPLIB/X/X-n701-k44.vrp) | 701 | 87 | 81923 |
| 120 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n716-k35](CVRPLIB/X/X-n716-k35.vrp) | 716 | 1007 | 43373 |
| 121 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n733-k159](CVRPLIB/X/X-n733-k159.vrp) | 733 | 25 | 136187 |
| 122 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n749-k98](CVRPLIB/X/X-n749-k98.vrp) | 749 | 396 | 77269 |
| 123 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n766-k71](CVRPLIB/X/X-n766-k71.vrp) | 766 | 166 | 114417 |
| 124 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n783-k48](CVRPLIB/X/X-n783-k48.vrp) | 783 | 832 | 72386 |
| 125 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n801-k40](CVRPLIB/X/X-n801-k40.vrp) | 801 | 20 | 73305 |
| 126 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n819-k171](CVRPLIB/X/X-n819-k171.vrp) | 819 | 358 | 158121 |
| 127 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n837-k142](CVRPLIB/X/X-n837-k142.vrp) | 837 | 44 | 193737 |
| 128 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n856-k95](CVRPLIB/X/X-n856-k95.vrp) | 856 | 9 | 88965 |
| 129 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n876-k59](CVRPLIB/X/X-n876-k59.vrp) | 876 | 764 | 99299 |
| 130 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n895-k37](CVRPLIB/X/X-n895-k37.vrp) | 895 | 1816 | 53860 |
| 131 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n916-k207](CVRPLIB/X/X-n916-k207.vrp) | 916 | 33 | 329179 |
| 132 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n936-k151](CVRPLIB/X/X-n936-k151.vrp) | 936 | 138 | 132715 |
| 133 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n957-k87](CVRPLIB/X/X-n957-k87.vrp) | 957 | 11 | 85465 |
| 134 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n979-k58](CVRPLIB/X/X-n979-k58.vrp) | 979 | 998 | 118976 |
| 135 | $\color{blue}{\textsf{S}}$ | CVRPLIB | [X/X-n1001-k43](CVRPLIB/X/X-n1001-k43.vrp) | 1001 | 131 | 72355 |
| 136 | $\color{blue}{\textsf{S}}$ | Synthetic | [XML1000_1123_01](Synthetic/XML1000_1123_01.vrp) | 1001 | 46 | — |
| 137 | $\color{blue}{\textsf{S}}$ | Synthetic | [XML1000_1173_01](Synthetic/XML1000_1173_01.vrp) | 1001 | 152 | — |
| 138 | $\color{blue}{\textsf{S}}$ | Synthetic | [XML1000_1176_01](Synthetic/XML1000_1176_01.vrp) | 1001 | 251 | — |
| 139 | $\color{blue}{\textsf{S}}$ | Synthetic | [XML1000_2113_01](Synthetic/XML1000_2113_01.vrp) | 1001 | 8 | — |
| 140 | $\color{blue}{\textsf{S}}$ | Synthetic | [XML1000_2121_01](Synthetic/XML1000_2121_01.vrp) | 1001 | 18 | — |
| 141 | $\color{blue}{\textsf{S}}$ | Synthetic | [XML1000_2122_01](Synthetic/XML1000_2122_01.vrp) | 1001 | 29 | — |
| 142 | $\color{blue}{\textsf{S}}$ | Synthetic | [XML1000_2123_01](Synthetic/XML1000_2123_01.vrp) | 1001 | 46 | — |
| 143 | $\color{blue}{\textsf{S}}$ | Synthetic | [XML1000_2124_01](Synthetic/XML1000_2124_01.vrp) | 1001 | 68 | — |
| 144 | $\color{blue}{\textsf{S}}$ | Synthetic | [XML1000_2125_01](Synthetic/XML1000_2125_01.vrp) | 1001 | 92 | — |
| 145 | $\color{blue}{\textsf{S}}$ | Synthetic | [XML1000_2126_01](Synthetic/XML1000_2126_01.vrp) | 1001 | 145 | — |
| 146 | $\color{blue}{\textsf{S}}$ | Synthetic | [XML1000_2133_01](Synthetic/XML1000_2133_01.vrp) | 1001 | 62 | — |
| 147 | $\color{blue}{\textsf{S}}$ | Synthetic | [XML1000_2143_01](Synthetic/XML1000_2143_01.vrp) | 1001 | 418 | — |
| 148 | $\color{blue}{\textsf{S}}$ | Synthetic | [XML1000_2153_01](Synthetic/XML1000_2153_01.vrp) | 1001 | 614 | — |
| 149 | $\color{blue}{\textsf{S}}$ | Synthetic | [XML1000_2163_01](Synthetic/XML1000_2163_01.vrp) | 1001 | 414 | — |
| 150 | $\color{blue}{\textsf{S}}$ | Synthetic | [XML1000_2173_01](Synthetic/XML1000_2173_01.vrp) | 1001 | 149 | — |
| 151 | $\color{blue}{\textsf{S}}$ | Synthetic | [XML1000_2176_01](Synthetic/XML1000_2176_01.vrp) | 1001 | 247 | — |
| 152 | $\color{blue}{\textsf{S}}$ | Synthetic | [XML1000_2223_01](Synthetic/XML1000_2223_01.vrp) | 1001 | 45 | — |
| 153 | $\color{blue}{\textsf{S}}$ | Synthetic | [XML1000_2323_01](Synthetic/XML1000_2323_01.vrp) | 1001 | 46 | — |
| 154 | $\color{blue}{\textsf{S}}$ | Synthetic | [XML1000_3123_01](Synthetic/XML1000_3123_01.vrp) | 1001 | 46 | — |
| 155 | $\color{purple}{\textsf{M}}$ | CVRPLIB | [AGS/Leuven1](CVRPLIB/AGS/Leuven1.vrp) | 3001 | 25 | 192848 |
| 156 | $\color{purple}{\textsf{M}}$ | CVRPLIB | [AGS/Leuven2](CVRPLIB/AGS/Leuven2.vrp) | 4001 | 150 | 111391 |
| 157 | $\color{purple}{\textsf{M}}$ | Synthetic | [XML5000_1173_01](Synthetic/XML5000_1173_01.vrp) | 5001 | 151 | — |
| 158 | $\color{purple}{\textsf{M}}$ | Synthetic | [XML5000_1176_01](Synthetic/XML5000_1176_01.vrp) | 5001 | 247 | — |
| 159 | $\color{purple}{\textsf{M}}$ | Synthetic | [XML5000_2123_01](Synthetic/XML5000_2123_01.vrp) | 5001 | 45 | — |
| 160 | $\color{purple}{\textsf{M}}$ | Synthetic | [XML5000_2126_01](Synthetic/XML5000_2126_01.vrp) | 5001 | 141 | — |
| 161 | $\color{purple}{\textsf{M}}$ | Synthetic | [XML5000_2173_01](Synthetic/XML5000_2173_01.vrp) | 5001 | 149 | — |
| 162 | $\color{purple}{\textsf{M}}$ | Synthetic | [XML5000_2176_01](Synthetic/XML5000_2176_01.vrp) | 5001 | 246 | — |
| 163 | $\color{purple}{\textsf{M}}$ | Synthetic | [XML5000_2323_01](Synthetic/XML5000_2323_01.vrp) | 5001 | 46 | — |
| 164 | $\color{purple}{\textsf{M}}$ | Synthetic | [XML5000_2326_01](Synthetic/XML5000_2326_01.vrp) | 5001 | 144 | — |
| 165 | $\color{purple}{\textsf{M}}$ | CVRPLIB | [AGS/Antwerp1](CVRPLIB/AGS/Antwerp1.vrp) | 6001 | 30 | 477277 |
| 166 | $\color{purple}{\textsf{M}}$ | CVRPLIB | [AGS/Antwerp2](CVRPLIB/AGS/Antwerp2.vrp) | 7001 | 100 | 291350 |
| 167 | $\color{purple}{\textsf{M}}$ | CVRPLIB | [AGS/Ghent1](CVRPLIB/AGS/Ghent1.vrp) | 10001 | 35 | 469531 |
| 168 | $\color{purple}{\textsf{M}}$ | Synthetic | [XML10000_1123_01](Synthetic/XML10000_1123_01.vrp) | 10001 | 45 | — |
| 169 | $\color{purple}{\textsf{M}}$ | Synthetic | [XML10000_1173_01](Synthetic/XML10000_1173_01.vrp) | 10001 | 148 | — |
| 170 | $\color{purple}{\textsf{M}}$ | Synthetic | [XML10000_1176_01](Synthetic/XML10000_1176_01.vrp) | 10001 | 245 | — |
| 171 | $\color{purple}{\textsf{M}}$ | Synthetic | [XML10000_2113_01](Synthetic/XML10000_2113_01.vrp) | 10001 | 8 | — |
| 172 | $\color{purple}{\textsf{M}}$ | Synthetic | [XML10000_2121_01](Synthetic/XML10000_2121_01.vrp) | 10001 | 17 | — |
| 173 | $\color{purple}{\textsf{M}}$ | Synthetic | [XML10000_2122_01](Synthetic/XML10000_2122_01.vrp) | 10001 | 28 | — |
| 174 | $\color{purple}{\textsf{M}}$ | Synthetic | [XML10000_2123_01](Synthetic/XML10000_2123_01.vrp) | 10001 | 45 | — |
| 175 | $\color{purple}{\textsf{M}}$ | Synthetic | [XML10000_2124_01](Synthetic/XML10000_2124_01.vrp) | 10001 | 66 | — |
| 176 | $\color{purple}{\textsf{M}}$ | Synthetic | [XML10000_2125_01](Synthetic/XML10000_2125_01.vrp) | 10001 | 89 | — |
| 177 | $\color{purple}{\textsf{M}}$ | Synthetic | [XML10000_2126_01](Synthetic/XML10000_2126_01.vrp) | 10001 | 141 | — |
| 178 | $\color{purple}{\textsf{M}}$ | Synthetic | [XML10000_2133_01](Synthetic/XML10000_2133_01.vrp) | 10001 | 61 | — |
| 179 | $\color{purple}{\textsf{M}}$ | Synthetic | [XML10000_2143_01](Synthetic/XML10000_2143_01.vrp) | 10001 | 406 | — |
| 180 | $\color{purple}{\textsf{M}}$ | Synthetic | [XML10000_2153_01](Synthetic/XML10000_2153_01.vrp) | 10001 | 608 | — |
| 181 | $\color{purple}{\textsf{M}}$ | Synthetic | [XML10000_2163_01](Synthetic/XML10000_2163_01.vrp) | 10001 | 409 | — |
| 182 | $\color{purple}{\textsf{M}}$ | Synthetic | [XML10000_2173_01](Synthetic/XML10000_2173_01.vrp) | 10001 | 148 | — |
| 183 | $\color{purple}{\textsf{M}}$ | Synthetic | [XML10000_2176_01](Synthetic/XML10000_2176_01.vrp) | 10001 | 245 | — |
| 184 | $\color{purple}{\textsf{M}}$ | Synthetic | [XML10000_2223_01](Synthetic/XML10000_2223_01.vrp) | 10001 | 45 | — |
| 185 | $\color{purple}{\textsf{M}}$ | Synthetic | [XML10000_2323_01](Synthetic/XML10000_2323_01.vrp) | 10001 | 45 | — |
| 186 | $\color{purple}{\textsf{M}}$ | Synthetic | [XML10000_3123_01](Synthetic/XML10000_3123_01.vrp) | 10001 | 45 | — |
| 187 | $\color{purple}{\textsf{M}}$ | Synthetic | [XML10000_3124_01](Synthetic/XML10000_3124_01.vrp) | 10001 | 67 | — |
| 188 | $\color{purple}{\textsf{M}}$ | Synthetic | [XML10000_3126_01](Synthetic/XML10000_3126_01.vrp) | 10001 | 141 | — |
| 189 | $\color{purple}{\textsf{M}}$ | Synthetic | [XML10000_3146_01](Synthetic/XML10000_3146_01.vrp) | 10001 | 1294 | — |
| 190 | $\color{orange}{\textsf{L}}$ | CVRPLIB | [AGS/Ghent2](CVRPLIB/AGS/Ghent2.vrp) | 11001 | 170 | 257748 |
| 191 | $\color{orange}{\textsf{L}}$ | CVRPLIB | [AGS/Brussels1](CVRPLIB/AGS/Brussels1.vrp) | 15001 | 50 | 501719 |
| 192 | $\color{orange}{\textsf{L}}$ | CVRPLIB | [AGS/Brussels2](CVRPLIB/AGS/Brussels2.vrp) | 16001 | 150 | 345468 |
| 193 | $\color{orange}{\textsf{L}}$ | FILO2 | [I/Valle-D-Aosta](FILO2/I/Valle-D-Aosta.vrp) | 20000 | 50 | 21679514 |
| 194 | $\color{orange}{\textsf{L}}$ | CVRPLIB | [AGS/Flanders1](CVRPLIB/AGS/Flanders1.vrp) | 20001 | 50 | 7240118 |
| 195 | $\color{orange}{\textsf{L}}$ | Synthetic | [XML20000_2123_01](Synthetic/XML20000_2123_01.vrp) | 20001 | 45 | — |
| 196 | $\color{orange}{\textsf{L}}$ | Synthetic | [XML20000_2126_01](Synthetic/XML20000_2126_01.vrp) | 20001 | 142 | — |
| 197 | $\color{orange}{\textsf{L}}$ | Synthetic | [XML20000_3123_01](Synthetic/XML20000_3123_01.vrp) | 20001 | 45 | — |
| 198 | $\color{orange}{\textsf{L}}$ | Synthetic | [XML20000_3126_01](Synthetic/XML20000_3126_01.vrp) | 20001 | 142 | — |
| 199 | $\color{orange}{\textsf{L}}$ | Synthetic | [XML25000_1173_01](Synthetic/XML25000_1173_01.vrp) | 25001 | 150 | — |
| 200 | $\color{orange}{\textsf{L}}$ | Synthetic | [XML25000_1176_01](Synthetic/XML25000_1176_01.vrp) | 25001 | 247 | — |
| 201 | $\color{orange}{\textsf{L}}$ | Synthetic | [XML25000_2173_01](Synthetic/XML25000_2173_01.vrp) | 25001 | 149 | — |
| 202 | $\color{orange}{\textsf{L}}$ | Synthetic | [XML25000_2176_01](Synthetic/XML25000_2176_01.vrp) | 25001 | 245 | — |
| 203 | $\color{orange}{\textsf{L}}$ | CVRPLIB | [AGS/Flanders2](CVRPLIB/AGS/Flanders2.vrp) | 30001 | 200 | 4373244 |
| 204 | $\color{orange}{\textsf{L}}$ | FILO2 | [I/Molise](FILO2/I/Molise.vrp) | 50000 | 50 | 111184982 |
| 205 | $\color{orange}{\textsf{L}}$ | Synthetic | [XML50000_1173_01](Synthetic/XML50000_1173_01.vrp) | 50001 | 150 | — |
| 206 | $\color{orange}{\textsf{L}}$ | Synthetic | [XML50000_1176_01](Synthetic/XML50000_1176_01.vrp) | 50001 | 247 | — |
| 207 | $\color{orange}{\textsf{L}}$ | Synthetic | [XML50000_2123_01](Synthetic/XML50000_2123_01.vrp) | 50001 | 45 | — |
| 208 | $\color{orange}{\textsf{L}}$ | Synthetic | [XML50000_2126_01](Synthetic/XML50000_2126_01.vrp) | 50001 | 142 | — |
| 209 | $\color{orange}{\textsf{L}}$ | Synthetic | [XML50000_2173_01](Synthetic/XML50000_2173_01.vrp) | 50001 | 149 | — |
| 210 | $\color{orange}{\textsf{L}}$ | Synthetic | [XML50000_2176_01](Synthetic/XML50000_2176_01.vrp) | 50001 | 247 | — |
| 211 | $\color{orange}{\textsf{L}}$ | Synthetic | [XML50000_3123_01](Synthetic/XML50000_3123_01.vrp) | 50001 | 45 | — |
| 212 | $\color{orange}{\textsf{L}}$ | Synthetic | [XML50000_3126_01](Synthetic/XML50000_3126_01.vrp) | 50001 | 142 | — |
| 213 | $\color{red}{\textsf{XL}}$ | Synthetic | [XML60000_1123_01](Synthetic/XML60000_1123_01.vrp) | 60001 | 45 | — |
| 214 | $\color{red}{\textsf{XL}}$ | Synthetic | [XML60000_1126_01](Synthetic/XML60000_1126_01.vrp) | 60001 | 143 | — |
| 215 | $\color{red}{\textsf{XL}}$ | Synthetic | [XML60000_2123_01](Synthetic/XML60000_2123_01.vrp) | 60001 | 45 | — |
| 216 | $\color{red}{\textsf{XL}}$ | Synthetic | [XML60000_2126_01](Synthetic/XML60000_2126_01.vrp) | 60001 | 143 | — |
| 217 | $\color{red}{\textsf{XL}}$ | Synthetic | [XML60000_3123_01](Synthetic/XML60000_3123_01.vrp) | 60001 | 45 | — |
| 218 | $\color{red}{\textsf{XL}}$ | Synthetic | [XML60000_3126_01](Synthetic/XML60000_3126_01.vrp) | 60001 | 143 | — |
| 219 | $\color{red}{\textsf{XL}}$ | Synthetic | [XML75000_1173_01](Synthetic/XML75000_1173_01.vrp) | 75001 | 149 | — |
| 220 | $\color{red}{\textsf{XL}}$ | Synthetic | [XML75000_1176_01](Synthetic/XML75000_1176_01.vrp) | 75001 | 247 | — |
| 221 | $\color{red}{\textsf{XL}}$ | Synthetic | [XML75000_2173_01](Synthetic/XML75000_2173_01.vrp) | 75001 | 149 | — |
| 222 | $\color{red}{\textsf{XL}}$ | Synthetic | [XML75000_2176_01](Synthetic/XML75000_2176_01.vrp) | 75001 | 247 | — |
| 223 | $\color{red}{\textsf{XL}}$ | Synthetic | [XML80000_1123_01](Synthetic/XML80000_1123_01.vrp) | 80001 | 45 | — |
| 224 | $\color{red}{\textsf{XL}}$ | Synthetic | [XML80000_1126_01](Synthetic/XML80000_1126_01.vrp) | 80001 | 142 | — |
| 225 | $\color{red}{\textsf{XL}}$ | Synthetic | [XML80000_2123_01](Synthetic/XML80000_2123_01.vrp) | 80001 | 45 | — |
| 226 | $\color{red}{\textsf{XL}}$ | Synthetic | [XML80000_2126_01](Synthetic/XML80000_2126_01.vrp) | 80001 | 142 | — |
| 227 | $\color{red}{\textsf{XL}}$ | Synthetic | [XML80000_3123_01](Synthetic/XML80000_3123_01.vrp) | 80001 | 45 | — |
| 228 | $\color{red}{\textsf{XL}}$ | Synthetic | [XML80000_3126_01](Synthetic/XML80000_3126_01.vrp) | 80001 | 142 | — |
| 229 | $\color{red}{\textsf{XL}}$ | FILO2 | [I/Trentino-Alto-Adige](FILO2/I/Trentino-Alto-Adige.vrp) | 100000 | 150 | 102063181 |
| 230 | $\color{red}{\textsf{XL}}$ | Synthetic | [XML100000_1123_01](Synthetic/XML100000_1123_01.vrp) | 100001 | 45 | — |
| 231 | $\color{red}{\textsf{XL}}$ | Synthetic | [XML100000_1173_01](Synthetic/XML100000_1173_01.vrp) | 100001 | 149 | — |
| 232 | $\color{red}{\textsf{XL}}$ | Synthetic | [XML100000_1176_01](Synthetic/XML100000_1176_01.vrp) | 100001 | 247 | — |
| 233 | $\color{red}{\textsf{XL}}$ | Synthetic | [XML100000_2113_01](Synthetic/XML100000_2113_01.vrp) | 100001 | 8 | — |
| 234 | $\color{red}{\textsf{XL}}$ | Synthetic | [XML100000_2121_01](Synthetic/XML100000_2121_01.vrp) | 100001 | 17 | — |
| 235 | $\color{red}{\textsf{XL}}$ | Synthetic | [XML100000_2122_01](Synthetic/XML100000_2122_01.vrp) | 100001 | 29 | — |
| 236 | $\color{red}{\textsf{XL}}$ | Synthetic | [XML100000_2123_01](Synthetic/XML100000_2123_01.vrp) | 100001 | 45 | — |
| 237 | $\color{red}{\textsf{XL}}$ | Synthetic | [XML100000_2124_01](Synthetic/XML100000_2124_01.vrp) | 100001 | 67 | — |
| 238 | $\color{red}{\textsf{XL}}$ | Synthetic | [XML100000_2125_01](Synthetic/XML100000_2125_01.vrp) | 100001 | 90 | — |
| 239 | $\color{red}{\textsf{XL}}$ | Synthetic | [XML100000_2126_01](Synthetic/XML100000_2126_01.vrp) | 100001 | 143 | — |
| 240 | $\color{red}{\textsf{XL}}$ | Synthetic | [XML100000_2133_01](Synthetic/XML100000_2133_01.vrp) | 100001 | 62 | — |
| 241 | $\color{red}{\textsf{XL}}$ | Synthetic | [XML100000_2143_01](Synthetic/XML100000_2143_01.vrp) | 100001 | 411 | — |
| 242 | $\color{red}{\textsf{XL}}$ | Synthetic | [XML100000_2153_01](Synthetic/XML100000_2153_01.vrp) | 100001 | 610 | — |
| 243 | $\color{red}{\textsf{XL}}$ | Synthetic | [XML100000_2163_01](Synthetic/XML100000_2163_01.vrp) | 100001 | 410 | — |
| 244 | $\color{red}{\textsf{XL}}$ | Synthetic | [XML100000_2173_01](Synthetic/XML100000_2173_01.vrp) | 100001 | 149 | — |
| 245 | $\color{red}{\textsf{XL}}$ | Synthetic | [XML100000_2176_01](Synthetic/XML100000_2176_01.vrp) | 100001 | 246 | — |
| 246 | $\color{red}{\textsf{XL}}$ | Synthetic | [XML100000_2223_01](Synthetic/XML100000_2223_01.vrp) | 100001 | 45 | — |
| 247 | $\color{red}{\textsf{XL}}$ | Synthetic | [XML100000_2323_01](Synthetic/XML100000_2323_01.vrp) | 100001 | 45 | — |
| 248 | $\color{red}{\textsf{XL}}$ | Synthetic | [XML100000_3123_01](Synthetic/XML100000_3123_01.vrp) | 100001 | 45 | — |
| 249 | $\color{red}{\textsf{XL}}$ | Synthetic | [XML100000_3126_01](Synthetic/XML100000_3126_01.vrp) | 100001 | 143 | — |
| 250 | $\color{teal}{\textsf{XXL}}$ | FILO2 | [I/Basilicata](FILO2/I/Basilicata.vrp) | 150000 | 150 | 175623919 |
| 251 | $\color{teal}{\textsf{XXL}}$ | FILO2 | [I/Umbria](FILO2/I/Umbria.vrp) | 200000 | 50 | 545507981 |
| 252 | $\color{teal}{\textsf{XXL}}$ | Synthetic | [XML200000_2123_01](Synthetic/XML200000_2123_01.vrp) | 200001 | 45 | — |
| 253 | $\color{teal}{\textsf{XXL}}$ | Synthetic | [XML200000_2126_01](Synthetic/XML200000_2126_01.vrp) | 200001 | 143 | — |
| 254 | $\color{teal}{\textsf{XXL}}$ | Synthetic | [XML200000_3123_01](Synthetic/XML200000_3123_01.vrp) | 200001 | 45 | — |
| 255 | $\color{teal}{\textsf{XXL}}$ | Synthetic | [XML200000_3126_01](Synthetic/XML200000_3126_01.vrp) | 200001 | 143 | — |
| 256 | $\color{teal}{\textsf{XXL}}$ | FILO2 | [I/Abruzzo](FILO2/I/Abruzzo.vrp) | 250000 | 200 | 311712556 |
| 257 | $\color{teal}{\textsf{XXL}}$ | FILO2 | [I/Friuli-Venezia-Giulia](FILO2/I/Friuli-Venezia-Giulia.vrp) | 300000 | 200 | 415805616 |
| 258 | $\color{teal}{\textsf{XXL}}$ | FILO2 | [I/Liguria](FILO2/I/Liguria.vrp) | 320000 | 50 | 1426389867 |
| 259 | $\color{teal}{\textsf{XXL}}$ | FILO2 | [I/Calabria](FILO2/I/Calabria.vrp) | 380000 | 50 | 1964651530 |
| 260 | $\color{teal}{\textsf{XXL}}$ | FILO2 | [I/Marche](FILO2/I/Marche.vrp) | 420000 | 200 | 420484426 |
| 261 | $\color{teal}{\textsf{XXL}}$ | FILO2 | [I/Sardegna](FILO2/I/Sardegna.vrp) | 470000 | 200 | 827934149 |
| 262 | $\color{teal}{\textsf{XXL}}$ | FILO2 | [I/Campania](FILO2/I/Campania.vrp) | 500000 | 200 | 391859276 |
| 263 | $\color{teal}{\textsf{XXL}}$ | Synthetic | [XML500000_1173_01](Synthetic/XML500000_1173_01.vrp) | 500001 | 150 | — |
| 264 | $\color{teal}{\textsf{XXL}}$ | Synthetic | [XML500000_1176_01](Synthetic/XML500000_1176_01.vrp) | 500001 | 247 | — |
| 265 | $\color{teal}{\textsf{XXL}}$ | Synthetic | [XML500000_2123_01](Synthetic/XML500000_2123_01.vrp) | 500001 | 45 | — |
| 266 | $\color{teal}{\textsf{XXL}}$ | Synthetic | [XML500000_2126_01](Synthetic/XML500000_2126_01.vrp) | 500001 | 143 | — |
| 267 | $\color{teal}{\textsf{XXL}}$ | Synthetic | [XML500000_2173_01](Synthetic/XML500000_2173_01.vrp) | 500001 | 150 | — |
| 268 | $\color{teal}{\textsf{XXL}}$ | Synthetic | [XML500000_2176_01](Synthetic/XML500000_2176_01.vrp) | 500001 | 247 | — |
| 269 | $\color{teal}{\textsf{XXL}}$ | Synthetic | [XML500000_3123_01](Synthetic/XML500000_3123_01.vrp) | 500001 | 45 | — |
| 270 | $\color{teal}{\textsf{XXL}}$ | Synthetic | [XML500000_3126_01](Synthetic/XML500000_3126_01.vrp) | 500001 | 143 | — |
| 271 | $\color{teal}{\textsf{XXL}}$ | FILO2 | [I/Piemonte](FILO2/I/Piemonte.vrp) | 600000 | 50 | 2627446164 |
| 272 | $\color{teal}{\textsf{XXL}}$ | FILO2 | [I/Toscana](FILO2/I/Toscana.vrp) | 700000 | 150 | 1084417188 |
| 273 | $\color{teal}{\textsf{XXL}}$ | Synthetic | [XML700000_2123_01](Synthetic/XML700000_2123_01.vrp) | 700001 | 45 | — |
| 274 | $\color{teal}{\textsf{XXL}}$ | Synthetic | [XML700000_2126_01](Synthetic/XML700000_2126_01.vrp) | 700001 | 142 | — |
| 275 | $\color{teal}{\textsf{XXL}}$ | Synthetic | [XML700000_3123_01](Synthetic/XML700000_3123_01.vrp) | 700001 | 45 | — |
| 276 | $\color{teal}{\textsf{XXL}}$ | Synthetic | [XML700000_3126_01](Synthetic/XML700000_3126_01.vrp) | 700001 | 142 | — |
| 277 | $\color{teal}{\textsf{XXL}}$ | FILO2 | [I/Puglia](FILO2/I/Puglia.vrp) | 750000 | 200 | 1464797603 |
| 278 | $\color{teal}{\textsf{XXL}}$ | FILO2 | [I/Sicilia](FILO2/I/Sicilia.vrp) | 800000 | 200 | 1774262462 |
| 279 | $\color{teal}{\textsf{XXL}}$ | FILO2 | [I/Veneto](FILO2/I/Veneto.vrp) | 850000 | 200 | 1050488613 |
| 280 | $\color{teal}{\textsf{XXL}}$ | FILO2 | [I/Emilia-Romagna](FILO2/I/Emilia-Romagna.vrp) | 900000 | 50 | 5405446715 |
| 281 | $\color{teal}{\textsf{XXL}}$ | FILO2 | [I/Lombardia](FILO2/I/Lombardia.vrp) | 950000 | 150 | 1339900081 |
| 282 | $\color{teal}{\textsf{XXL}}$ | FILO2 | [I/Lazio](FILO2/I/Lazio.vrp) | 1000000 | 50 | 3145381332 |
| 283 | $\color{teal}{\textsf{XXL}}$ | Synthetic | [XML1000000_1173_01](Synthetic/XML1000000_1173_01.vrp) | 1000001 | 150 | — |
| 284 | $\color{teal}{\textsf{XXL}}$ | Synthetic | [XML1000000_1176_01](Synthetic/XML1000000_1176_01.vrp) | 1000001 | 247 | — |
| 285 | $\color{teal}{\textsf{XXL}}$ | Synthetic | [XML1000000_2123_01](Synthetic/XML1000000_2123_01.vrp) | 1000001 | 45 | — |
| 286 | $\color{teal}{\textsf{XXL}}$ | Synthetic | [XML1000000_2126_01](Synthetic/XML1000000_2126_01.vrp) | 1000001 | 142 | — |
| 287 | $\color{teal}{\textsf{XXL}}$ | Synthetic | [XML1000000_2173_01](Synthetic/XML1000000_2173_01.vrp) | 1000001 | 150 | — |
| 288 | $\color{teal}{\textsf{XXL}}$ | Synthetic | [XML1000000_2176_01](Synthetic/XML1000000_2176_01.vrp) | 1000001 | 247 | — |
| 289 | $\color{teal}{\textsf{XXL}}$ | Synthetic | [XML1000000_3123_01](Synthetic/XML1000000_3123_01.vrp) | 1000001 | 45 | — |
| 290 | $\color{teal}{\textsf{XXL}}$ | Synthetic | [XML1000000_3126_01](Synthetic/XML1000000_3126_01.vrp) | 1000001 | 142 | — |
| 291 | $\color{magenta}{\textsf{XXXL}}$ | Synthetic | [XML1500000_1173_01](Synthetic/XML1500000_1173_01.vrp) | 1500001 | 149 | — |
| 292 | $\color{magenta}{\textsf{XXXL}}$ | Synthetic | [XML1500000_1176_01](Synthetic/XML1500000_1176_01.vrp) | 1500001 | 247 | — |
| 293 | $\color{magenta}{\textsf{XXXL}}$ | Synthetic | [XML2000000_1113_01](Synthetic/XML2000000_1113_01.vrp) | 2000001 | 8 | — |
| 294 | $\color{magenta}{\textsf{XXXL}}$ | Synthetic | [XML2000000_1121_01](Synthetic/XML2000000_1121_01.vrp) | 2000001 | 17 | — |
| 295 | $\color{magenta}{\textsf{XXXL}}$ | Synthetic | [XML2000000_1123_01](Synthetic/XML2000000_1123_01.vrp) | 2000001 | 45 | — |
| 296 | $\color{magenta}{\textsf{XXXL}}$ | Synthetic | [XML2000000_1126_01](Synthetic/XML2000000_1126_01.vrp) | 2000001 | 142 | — |
| 297 | $\color{magenta}{\textsf{XXXL}}$ | Synthetic | [XML2000000_1173_01](Synthetic/XML2000000_1173_01.vrp) | 2000001 | 149 | — |
| 298 | $\color{magenta}{\textsf{XXXL}}$ | Synthetic | [XML2000000_1176_01](Synthetic/XML2000000_1176_01.vrp) | 2000001 | 247 | — |
| 299 | $\color{magenta}{\textsf{XXXL}}$ | Synthetic | [XML2000000_2113_01](Synthetic/XML2000000_2113_01.vrp) | 2000001 | 8 | — |
| 300 | $\color{magenta}{\textsf{XXXL}}$ | Synthetic | [XML2000000_2121_01](Synthetic/XML2000000_2121_01.vrp) | 2000001 | 17 | — |
| 301 | $\color{magenta}{\textsf{XXXL}}$ | Synthetic | [XML2000000_2122_01](Synthetic/XML2000000_2122_01.vrp) | 2000001 | 29 | — |
| 302 | $\color{magenta}{\textsf{XXXL}}$ | Synthetic | [XML2000000_2123_01](Synthetic/XML2000000_2123_01.vrp) | 2000001 | 45 | — |
| 303 | $\color{magenta}{\textsf{XXXL}}$ | Synthetic | [XML2000000_2124_01](Synthetic/XML2000000_2124_01.vrp) | 2000001 | 67 | — |
| 304 | $\color{magenta}{\textsf{XXXL}}$ | Synthetic | [XML2000000_2125_01](Synthetic/XML2000000_2125_01.vrp) | 2000001 | 90 | — |
| 305 | $\color{magenta}{\textsf{XXXL}}$ | Synthetic | [XML2000000_2126_01](Synthetic/XML2000000_2126_01.vrp) | 2000001 | 142 | — |
| 306 | $\color{magenta}{\textsf{XXXL}}$ | Synthetic | [XML2000000_2133_01](Synthetic/XML2000000_2133_01.vrp) | 2000001 | 61 | — |
| 307 | $\color{magenta}{\textsf{XXXL}}$ | Synthetic | [XML2000000_2143_01](Synthetic/XML2000000_2143_01.vrp) | 2000001 | 411 | — |
| 308 | $\color{magenta}{\textsf{XXXL}}$ | Synthetic | [XML2000000_2153_01](Synthetic/XML2000000_2153_01.vrp) | 2000001 | 610 | — |
| 309 | $\color{magenta}{\textsf{XXXL}}$ | Synthetic | [XML2000000_2163_01](Synthetic/XML2000000_2163_01.vrp) | 2000001 | 411 | — |
| 310 | $\color{magenta}{\textsf{XXXL}}$ | Synthetic | [XML2000000_2173_01](Synthetic/XML2000000_2173_01.vrp) | 2000001 | 149 | — |
| 311 | $\color{magenta}{\textsf{XXXL}}$ | Synthetic | [XML2000000_2176_01](Synthetic/XML2000000_2176_01.vrp) | 2000001 | 247 | — |
| 312 | $\color{magenta}{\textsf{XXXL}}$ | Synthetic | [XML2000000_2223_01](Synthetic/XML2000000_2223_01.vrp) | 2000001 | 45 | — |
| 313 | $\color{magenta}{\textsf{XXXL}}$ | Synthetic | [XML2000000_2323_01](Synthetic/XML2000000_2323_01.vrp) | 2000001 | 45 | — |
| 314 | $\color{magenta}{\textsf{XXXL}}$ | Synthetic | [XML2000000_3113_01](Synthetic/XML2000000_3113_01.vrp) | 2000001 | 8 | — |
| 315 | $\color{magenta}{\textsf{XXXL}}$ | Synthetic | [XML2000000_3121_01](Synthetic/XML2000000_3121_01.vrp) | 2000001 | 17 | — |
| 316 | $\color{magenta}{\textsf{XXXL}}$ | Synthetic | [XML2000000_3123_01](Synthetic/XML2000000_3123_01.vrp) | 2000001 | 45 | — |
| 317 | $\color{magenta}{\textsf{XXXL}}$ | Synthetic | [XML2000000_3126_01](Synthetic/XML2000000_3126_01.vrp) | 2000001 | 142 | — |
| 318 | $\color{magenta}{\textsf{XXXL}}$ | Synthetic | [XML2000000_3161_01](Synthetic/XML2000000_3161_01.vrp) | 2000001 | 155 | — |
| 319 | $\color{magenta}{\textsf{XXXL}}$ | Synthetic | [XML2000000_3173_01](Synthetic/XML2000000_3173_01.vrp) | 2000001 | 149 | — |
| 320 | $\color{magenta}{\textsf{XXXL}}$ | Synthetic | [XML2000000_3176_01](Synthetic/XML2000000_3176_01.vrp) | 2000001 | 247 | — |

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
