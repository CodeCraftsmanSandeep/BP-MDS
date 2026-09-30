# Input Instances

Capacity-only CVRP benchmarks from CVRPLIB, FILO2, and Synthetic XML-style instances *(CVRPLIB & FILO2 accessed 15 April 2026)*.

**Total** 310  ·  **CVRPLIB** 130  ·  **FILO2** 20  ·  **Synthetic** 160

🟢 **XS** 18  ·  🟡 **S** 137  ·  🟣 **M** 28  ·  🟠 **L** 15  ·  🔴 **XL** 38  ·  🔵 **XXL** 41  ·  🟤 **XXXL** 33

Machine-readable index: [`instances.csv`](instances.csv)

**Note:** Only `Sample/` ships in-repo for quick checks. **CVRPLIB**, **FILO2**, and **Synthetic** `.vrp` files are distributed as zip assets on [GitHub Releases](https://github.com/CodeCraftsmanSandeep/BP-MDS/releases) — unpack under `Inputs/CVRPLIB/`, `Inputs/FILO2/`, and `Inputs/Synthetic/` locally (those folders are gitignored).

---

## Instances


| Symbol       | Meaning                                          |
| ------------ | ------------------------------------------------ |
| **Size**     | By **#Customers** (`N−1`)                        |
| **Source**   | `CVRPLIB` · `FILO2` · `Synthetic`                |
| **Instance** | Name / path (instance `.vrp` files via GitHub Releases) |
| **N**        | `#Customers + 1` (= `DIMENSION`, includes depot) |
| **Q**        | Vehicle capacity                                 |
| **BKS**      | Best-known solution cost (if available)          |



| S.No | Size    | Source    | Instance                                                     | N       | Q    | BKS           |
| ---- | ------- | --------- | ------------------------------------------------------------ | ------- | ---- | ------------- |
| 1    | 🟢 XS   | Synthetic | XML10_1173_01                 | 11      | 50   | —             |
| 2    | 🟢 XS   | Synthetic | XML10_1176_01                 | 11      | 158  | —             |
| 3    | 🟢 XS   | Synthetic | XML10_2173_01                 | 11      | 35   | —             |
| 4    | 🟢 XS   | Synthetic | XML10_2176_01                 | 11      | 112  | —             |
| 5    | 🟢 XS   | Synthetic | XML50_1173_01                 | 51      | 145  | —             |
| 6    | 🟢 XS   | Synthetic | XML50_1176_01                 | 51      | 198  | —             |
| 7    | 🟢 XS   | Synthetic | XML50_2173_01                 | 51      | 138  | —             |
| 8    | 🟢 XS   | Synthetic | XML50_2176_01                 | 51      | 182  | —             |
| 9    | 🟢 XS   | CVRPLIB   | E/E-n76-k10                       | 76      | 140  | 830.00        |
| 10   | 🟢 XS   | CVRPLIB   | E/E-n76-k14                       | 76      | 100  | 1021.00       |
| 11   | 🟢 XS   | CVRPLIB   | E/E-n101-k14                     | 101     | 112  | 1067.00       |
| 12   | 🟢 XS   | CVRPLIB   | E/E-n101-k8                       | 101     | 200  | 815.00        |
| 13   | 🟢 XS   | CVRPLIB   | P/P-n101-k4                       | 101     | 400  | 681.00        |
| 14   | 🟢 XS   | CVRPLIB   | X/X-n101-k25                     | 101     | 206  | 27591.00      |
| 15   | 🟢 XS   | Synthetic | XML100_1173_01               | 101     | 133  | —             |
| 16   | 🟢 XS   | Synthetic | XML100_1176_01               | 101     | 209  | —             |
| 17   | 🟢 XS   | Synthetic | XML100_2173_01               | 101     | 152  | —             |
| 18   | 🟢 XS   | Synthetic | XML100_2176_01               | 101     | 240  | —             |
| 19   | 🟡 S    | CVRPLIB   | X/X-n106-k14                     | 106     | 600  | 26362.00      |
| 20   | 🟡 S    | CVRPLIB   | X/X-n110-k13                     | 110     | 66   | 14971.00      |
| 21   | 🟡 S    | CVRPLIB   | X/X-n115-k10                     | 115     | 169  | 12747.00      |
| 22   | 🟡 S    | CVRPLIB   | X/X-n120-k6                       | 120     | 21   | 13332.00      |
| 23   | 🟡 S    | CVRPLIB   | X/X-n125-k30                     | 125     | 188  | 55539.00      |
| 24   | 🟡 S    | CVRPLIB   | X/X-n129-k18                     | 129     | 39   | 28940.00      |
| 25   | 🟡 S    | CVRPLIB   | X/X-n134-k13                     | 134     | 643  | 10916.00      |
| 26   | 🟡 S    | CVRPLIB   | F/F-n135-k7                       | 135     | 2210 | 1162.00       |
| 27   | 🟡 S    | CVRPLIB   | X/X-n139-k10                     | 139     | 106  | 13590.00      |
| 28   | 🟡 S    | CVRPLIB   | X/X-n143-k7                       | 143     | 1190 | 15700.00      |
| 29   | 🟡 S    | CVRPLIB   | X/X-n148-k46                     | 148     | 18   | 43448.00      |
| 30   | 🟡 S    | CVRPLIB   | X/X-n153-k22                     | 153     | 144  | 21220.00      |
| 31   | 🟡 S    | CVRPLIB   | X/X-n157-k13                     | 157     | 12   | 16876.00      |
| 32   | 🟡 S    | CVRPLIB   | X/X-n162-k11                     | 162     | 1174 | 14138.00      |
| 33   | 🟡 S    | CVRPLIB   | X/X-n167-k10                     | 167     | 133  | 20557.00      |
| 34   | 🟡 S    | CVRPLIB   | X/X-n172-k51                     | 172     | 161  | 45607.00      |
| 35   | 🟡 S    | CVRPLIB   | X/X-n176-k26                     | 176     | 142  | 47812.00      |
| 36   | 🟡 S    | CVRPLIB   | X/X-n181-k23                     | 181     | 8    | 25569.00      |
| 37   | 🟡 S    | CVRPLIB   | X/X-n186-k15                     | 186     | 974  | 24145.00      |
| 38   | 🟡 S    | CVRPLIB   | X/X-n190-k8                       | 190     | 138  | 16980.00      |
| 39   | 🟡 S    | CVRPLIB   | X/X-n195-k51                     | 195     | 181  | 44225.00      |
| 40   | 🟡 S    | CVRPLIB   | CMT/CMT5                             | 200     | 200  | 1291.29       |
| 41   | 🟡 S    | CVRPLIB   | X/X-n200-k36                     | 200     | 402  | 58578.00      |
| 42   | 🟡 S    | CVRPLIB   | X/X-n204-k19                     | 204     | 836  | 19565.00      |
| 43   | 🟡 S    | CVRPLIB   | X/X-n209-k16                     | 209     | 101  | 30656.00      |
| 44   | 🟡 S    | CVRPLIB   | X/X-n214-k11                     | 214     | 944  | 10856.00      |
| 45   | 🟡 S    | CVRPLIB   | X/X-n219-k73                     | 219     | 3    | 117595.00     |
| 46   | 🟡 S    | CVRPLIB   | X/X-n223-k34                     | 223     | 37   | 40437.00      |
| 47   | 🟡 S    | CVRPLIB   | X/X-n228-k23                     | 228     | 154  | 25742.00      |
| 48   | 🟡 S    | CVRPLIB   | X/X-n233-k16                     | 233     | 631  | 19230.00      |
| 49   | 🟡 S    | CVRPLIB   | X/X-n237-k14                     | 237     | 18   | 27042.00      |
| 50   | 🟡 S    | CVRPLIB   | Golden/Golden_17             | 241     | 200  | 707.76        |
| 51   | 🟡 S    | CVRPLIB   | X/X-n242-k48                     | 242     | 28   | 82751.00      |
| 52   | 🟡 S    | CVRPLIB   | X/X-n247-k50                     | 247     | 134  | 37274.00      |
| 53   | 🟡 S    | CVRPLIB   | X/X-n251-k28                     | 251     | 69   | 38684.00      |
| 54   | 🟡 S    | CVRPLIB   | Golden/Golden_13             | 253     | 1000 | 857.19        |
| 55   | 🟡 S    | CVRPLIB   | Golden/Golden_9               | 256     | 1000 | 579.70        |
| 56   | 🟡 S    | CVRPLIB   | X/X-n256-k16                     | 256     | 1225 | 18839.00      |
| 57   | 🟡 S    | CVRPLIB   | X/X-n261-k13                     | 261     | 1081 | 26558.00      |
| 58   | 🟡 S    | CVRPLIB   | X/X-n266-k58                     | 266     | 35   | 75478.00      |
| 59   | 🟡 S    | CVRPLIB   | X/X-n270-k35                     | 270     | 585  | 35291.00      |
| 60   | 🟡 S    | CVRPLIB   | X/X-n275-k28                     | 275     | 10   | 21245.00      |
| 61   | 🟡 S    | CVRPLIB   | X/X-n280-k17                     | 280     | 192  | 33503.00      |
| 62   | 🟡 S    | CVRPLIB   | X/X-n284-k15                     | 284     | 109  | 20215.00      |
| 63   | 🟡 S    | CVRPLIB   | X/X-n289-k60                     | 289     | 267  | 95151.00      |
| 64   | 🟡 S    | CVRPLIB   | X/X-n294-k50                     | 294     | 285  | 47161.00      |
| 65   | 🟡 S    | CVRPLIB   | X/X-n298-k31                     | 298     | 55   | 34231.00      |
| 66   | 🟡 S    | CVRPLIB   | Golden/Golden_18             | 301     | 200  | 995.13        |
| 67   | 🟡 S    | CVRPLIB   | X/X-n303-k21                     | 303     | 794  | 21736.00      |
| 68   | 🟡 S    | CVRPLIB   | X/X-n308-k13                     | 308     | 246  | 25859.00      |
| 69   | 🟡 S    | CVRPLIB   | X/X-n313-k71                     | 313     | 248  | 94043.00      |
| 70   | 🟡 S    | CVRPLIB   | X/X-n317-k53                     | 317     | 6    | 78355.00      |
| 71   | 🟡 S    | CVRPLIB   | Golden/Golden_14             | 321     | 1000 | 1080.55       |
| 72   | 🟡 S    | CVRPLIB   | X/X-n322-k28                     | 322     | 868  | 29834.00      |
| 73   | 🟡 S    | CVRPLIB   | Golden/Golden_10             | 324     | 1000 | 735.43        |
| 74   | 🟡 S    | CVRPLIB   | X/X-n327-k20                     | 327     | 128  | 27532.00      |
| 75   | 🟡 S    | CVRPLIB   | X/X-n331-k15                     | 331     | 23   | 31102.00      |
| 76   | 🟡 S    | CVRPLIB   | X/X-n336-k84                     | 336     | 203  | 139111.00     |
| 77   | 🟡 S    | CVRPLIB   | X/X-n344-k43                     | 344     | 61   | 42050.00      |
| 78   | 🟡 S    | CVRPLIB   | X/X-n351-k40                     | 351     | 436  | 25896.00      |
| 79   | 🟡 S    | CVRPLIB   | X/X-n359-k29                     | 359     | 68   | 51505.00      |
| 80   | 🟡 S    | CVRPLIB   | Golden/Golden_19             | 361     | 200  | 1365.60       |
| 81   | 🟡 S    | CVRPLIB   | X/X-n367-k17                     | 367     | 218  | 22814.00      |
| 82   | 🟡 S    | CVRPLIB   | X/X-n376-k94                     | 376     | 4    | 147713.00     |
| 83   | 🟡 S    | CVRPLIB   | X/X-n384-k52                     | 384     | 564  | 65928.00      |
| 84   | 🟡 S    | CVRPLIB   | tai/tai385                         | 386     | 65   | 24366.41      |
| 85   | 🟡 S    | CVRPLIB   | X/X-n393-k38                     | 393     | 78   | 38260.00      |
| 86   | 🟡 S    | CVRPLIB   | Golden/Golden_15             | 397     | 1000 | 1337.27       |
| 87   | 🟡 S    | CVRPLIB   | Golden/Golden_11             | 400     | 1000 | 911.98        |
| 88   | 🟡 S    | CVRPLIB   | X/X-n401-k29                     | 401     | 745  | 66154.00      |
| 89   | 🟡 S    | CVRPLIB   | X/X-n411-k19                     | 411     | 216  | 19712.00      |
| 90   | 🟡 S    | CVRPLIB   | X/X-n420-k130                   | 420     | 18   | 107798.00     |
| 91   | 🟡 S    | CVRPLIB   | Golden/Golden_20             | 421     | 200  | 1817.59       |
| 92   | 🟡 S    | CVRPLIB   | X/X-n429-k61                     | 429     | 536  | 65449.00      |
| 93   | 🟡 S    | CVRPLIB   | X/X-n439-k37                     | 439     | 12   | 36391.00      |
| 94   | 🟡 S    | CVRPLIB   | X/X-n449-k29                     | 449     | 777  | 55233.00      |
| 95   | 🟡 S    | CVRPLIB   | X/X-n459-k26                     | 459     | 1106 | 24139.00      |
| 96   | 🟡 S    | CVRPLIB   | X/X-n469-k138                   | 469     | 256  | 221824.00     |
| 97   | 🟡 S    | CVRPLIB   | X/X-n480-k70                     | 480     | 52   | 89449.00      |
| 98   | 🟡 S    | CVRPLIB   | Golden/Golden_16             | 481     | 1000 | 1611.28       |
| 99   | 🟡 S    | CVRPLIB   | Golden/Golden_12             | 484     | 1000 | 1100.67       |
| 100  | 🟡 S    | CVRPLIB   | X/X-n491-k59                     | 491     | 428  | 66483.00      |
| 101  | 🟡 S    | Synthetic | XML500_1173_01               | 501     | 146  | —             |
| 102  | 🟡 S    | Synthetic | XML500_1176_01               | 501     | 242  | —             |
| 103  | 🟡 S    | Synthetic | XML500_2173_01               | 501     | 150  | —             |
| 104  | 🟡 S    | Synthetic | XML500_2176_01               | 501     | 244  | —             |
| 105  | 🟡 S    | CVRPLIB   | X/X-n502-k39                     | 502     | 13   | 69226.00      |
| 106  | 🟡 S    | CVRPLIB   | X/X-n513-k21                     | 513     | 142  | 24201.00      |
| 107  | 🟡 S    | CVRPLIB   | X/X-n524-k153                   | 524     | 125  | 154593.00     |
| 108  | 🟡 S    | CVRPLIB   | X/X-n536-k96                     | 536     | 371  | 94846.00      |
| 109  | 🟡 S    | CVRPLIB   | X/X-n548-k50                     | 548     | 11   | 86700.00      |
| 110  | 🟡 S    | CVRPLIB   | X/X-n561-k42                     | 561     | 74   | 42717.00      |
| 111  | 🟡 S    | CVRPLIB   | X/X-n573-k30                     | 573     | 210  | 50673.00      |
| 112  | 🟡 S    | CVRPLIB   | X/X-n586-k159                   | 586     | 28   | 190316.00     |
| 113  | 🟡 S    | CVRPLIB   | X/X-n599-k92                     | 599     | 487  | 108451.00     |
| 114  | 🟡 S    | CVRPLIB   | X/X-n613-k62                     | 613     | 523  | 59535.00      |
| 115  | 🟡 S    | CVRPLIB   | X/X-n627-k43                     | 627     | 110  | 62164.00      |
| 116  | 🟡 S    | CVRPLIB   | X/X-n641-k35                     | 641     | 1381 | 63682.00      |
| 117  | 🟡 S    | CVRPLIB   | X/X-n655-k131                   | 655     | 5    | 106780.00     |
| 118  | 🟡 S    | CVRPLIB   | X/X-n670-k130                   | 670     | 129  | 146332.00     |
| 119  | 🟡 S    | CVRPLIB   | X/X-n685-k75                     | 685     | 408  | 68205.00      |
| 120  | 🟡 S    | CVRPLIB   | X/X-n701-k44                     | 701     | 87   | 81923.00      |
| 121  | 🟡 S    | CVRPLIB   | X/X-n716-k35                     | 716     | 1007 | 43373.00      |
| 122  | 🟡 S    | CVRPLIB   | X/X-n733-k159                   | 733     | 25   | 136187.00     |
| 123  | 🟡 S    | CVRPLIB   | X/X-n749-k98                     | 749     | 396  | 77269.00      |
| 124  | 🟡 S    | CVRPLIB   | X/X-n766-k71                     | 766     | 166  | 114417.00     |
| 125  | 🟡 S    | CVRPLIB   | X/X-n783-k48                     | 783     | 832  | 72386.00      |
| 126  | 🟡 S    | CVRPLIB   | X/X-n801-k40                     | 801     | 20   | 73305.00      |
| 127  | 🟡 S    | CVRPLIB   | X/X-n819-k171                   | 819     | 358  | 158121.00     |
| 128  | 🟡 S    | CVRPLIB   | X/X-n837-k142                   | 837     | 44   | 193737.00     |
| 129  | 🟡 S    | CVRPLIB   | X/X-n856-k95                     | 856     | 9    | 88965.00      |
| 130  | 🟡 S    | CVRPLIB   | X/X-n876-k59                     | 876     | 764  | 99299.00      |
| 131  | 🟡 S    | CVRPLIB   | X/X-n895-k37                     | 895     | 1816 | 53860.00      |
| 132  | 🟡 S    | CVRPLIB   | X/X-n916-k207                   | 916     | 33   | 329179.00     |
| 133  | 🟡 S    | CVRPLIB   | X/X-n936-k151                   | 936     | 138  | 132715.00     |
| 134  | 🟡 S    | CVRPLIB   | X/X-n957-k87                     | 957     | 11   | 85465.00      |
| 135  | 🟡 S    | CVRPLIB   | X/X-n979-k58                     | 979     | 998  | 118976.00     |
| 136  | 🟡 S    | CVRPLIB   | X/X-n1001-k43                   | 1001    | 131  | 72355.00      |
| 137  | 🟡 S    | Synthetic | XML1000_1123_01             | 1001    | 46   | —             |
| 138  | 🟡 S    | Synthetic | XML1000_1173_01             | 1001    | 148  | —             |
| 139  | 🟡 S    | Synthetic | XML1000_1176_01             | 1001    | 240  | —             |
| 140  | 🟡 S    | Synthetic | XML1000_2113_01             | 1001    | 8    | —             |
| 141  | 🟡 S    | Synthetic | XML1000_2121_01             | 1001    | 18   | —             |
| 142  | 🟡 S    | Synthetic | XML1000_2122_01             | 1001    | 29   | —             |
| 143  | 🟡 S    | Synthetic | XML1000_2123_01             | 1001    | 46   | —             |
| 144  | 🟡 S    | Synthetic | XML1000_2124_01             | 1001    | 68   | —             |
| 145  | 🟡 S    | Synthetic | XML1000_2125_01             | 1001    | 92   | —             |
| 146  | 🟡 S    | Synthetic | XML1000_2126_01             | 1001    | 145  | —             |
| 147  | 🟡 S    | Synthetic | XML1000_2133_01             | 1001    | 62   | —             |
| 148  | 🟡 S    | Synthetic | XML1000_2143_01             | 1001    | 418  | —             |
| 149  | 🟡 S    | Synthetic | XML1000_2153_01             | 1001    | 614  | —             |
| 150  | 🟡 S    | Synthetic | XML1000_2163_01             | 1001    | 414  | —             |
| 151  | 🟡 S    | Synthetic | XML1000_2173_01             | 1001    | 149  | —             |
| 152  | 🟡 S    | Synthetic | XML1000_2176_01             | 1001    | 251  | —             |
| 153  | 🟡 S    | Synthetic | XML1000_2223_01             | 1001    | 46   | —             |
| 154  | 🟡 S    | Synthetic | XML1000_2323_01             | 1001    | 45   | —             |
| 155  | 🟡 S    | Synthetic | XML1000_3123_01             | 1001    | 46   | —             |
| 156  | 🟣 M    | CVRPLIB   | AGS/Leuven1                       | 3001    | 25   | 192848.00     |
| 157  | 🟣 M    | CVRPLIB   | AGS/Leuven2                       | 4001    | 150  | 111391.00     |
| 158  | 🟣 M    | Synthetic | XML5000_1173_01             | 5001    | 149  | —             |
| 159  | 🟣 M    | Synthetic | XML5000_1176_01             | 5001    | 246  | —             |
| 160  | 🟣 M    | Synthetic | XML5000_2173_01             | 5001    | 149  | —             |
| 161  | 🟣 M    | Synthetic | XML5000_2176_01             | 5001    | 244  | —             |
| 162  | 🟣 M    | CVRPLIB   | AGS/Antwerp1                     | 6001    | 30   | 477277.00     |
| 163  | 🟣 M    | CVRPLIB   | AGS/Antwerp2                     | 7001    | 100  | 291350.00     |
| 164  | 🟣 M    | CVRPLIB   | AGS/Ghent1                         | 10001   | 35   | 469531.00     |
| 165  | 🟣 M    | Synthetic | XML10000_1123_01           | 10001   | 45   | —             |
| 166  | 🟣 M    | Synthetic | XML10000_1173_01           | 10001   | 148  | —             |
| 167  | 🟣 M    | Synthetic | XML10000_1176_01           | 10001   | 244  | —             |
| 168  | 🟣 M    | Synthetic | XML10000_2113_01           | 10001   | 8    | —             |
| 169  | 🟣 M    | Synthetic | XML10000_2121_01           | 10001   | 17   | —             |
| 170  | 🟣 M    | Synthetic | XML10000_2122_01           | 10001   | 28   | —             |
| 171  | 🟣 M    | Synthetic | XML10000_2123_01           | 10001   | 45   | —             |
| 172  | 🟣 M    | Synthetic | XML10000_2124_01           | 10001   | 66   | —             |
| 173  | 🟣 M    | Synthetic | XML10000_2125_01           | 10001   | 89   | —             |
| 174  | 🟣 M    | Synthetic | XML10000_2126_01           | 10001   | 141  | —             |
| 175  | 🟣 M    | Synthetic | XML10000_2133_01           | 10001   | 61   | —             |
| 176  | 🟣 M    | Synthetic | XML10000_2143_01           | 10001   | 406  | —             |
| 177  | 🟣 M    | Synthetic | XML10000_2153_01           | 10001   | 608  | —             |
| 178  | 🟣 M    | Synthetic | XML10000_2163_01           | 10001   | 409  | —             |
| 179  | 🟣 M    | Synthetic | XML10000_2173_01           | 10001   | 148  | —             |
| 180  | 🟣 M    | Synthetic | XML10000_2176_01           | 10001   | 248  | —             |
| 181  | 🟣 M    | Synthetic | XML10000_2223_01           | 10001   | 45   | —             |
| 182  | 🟣 M    | Synthetic | XML10000_2323_01           | 10001   | 45   | —             |
| 183  | 🟣 M    | Synthetic | XML10000_3123_01           | 10001   | 45   | —             |
| 184  | 🟠 L    | CVRPLIB   | AGS/Ghent2                         | 11001   | 170  | 257748.00     |
| 185  | 🟠 L    | CVRPLIB   | AGS/Brussels1                   | 15001   | 50   | 501719.00     |
| 186  | 🟠 L    | CVRPLIB   | AGS/Brussels2                   | 16001   | 150  | 345468.00     |
| 187  | 🟠 L    | FILO2     | I/Valle-D-Aosta                 | 20000   | 50   | 21679514.00   |
| 188  | 🟠 L    | CVRPLIB   | AGS/Flanders1                   | 20001   | 50   | 7240118.00    |
| 189  | 🟠 L    | Synthetic | XML25000_1173_01           | 25001   | 150  | —             |
| 190  | 🟠 L    | Synthetic | XML25000_1176_01           | 25001   | 247  | —             |
| 191  | 🟠 L    | Synthetic | XML25000_2173_01           | 25001   | 149  | —             |
| 192  | 🟠 L    | Synthetic | XML25000_2176_01           | 25001   | 247  | —             |
| 193  | 🟠 L    | CVRPLIB   | AGS/Flanders2                   | 30001   | 200  | 4373244.00    |
| 194  | 🟠 L    | FILO2     | I/Molise                               | 50000   | 50   | 111184982.00  |
| 195  | 🟠 L    | Synthetic | XML50000_1173_01           | 50001   | 149  | —             |
| 196  | 🟠 L    | Synthetic | XML50000_1176_01           | 50001   | 246  | —             |
| 197  | 🟠 L    | Synthetic | XML50000_2173_01           | 50001   | 150  | —             |
| 198  | 🟠 L    | Synthetic | XML50000_2176_01           | 50001   | 247  | —             |
| 199  | 🔴 XL   | Synthetic | XML60000_1123_01           | 60001   | 54   | —             |
| 200  | 🔴 XL   | Synthetic | XML60000_1126_01           | 60001   | 197  | —             |
| 201  | 🔴 XL   | Synthetic | XML60000_2123_01           | 60001   | 54   | —             |
| 202  | 🔴 XL   | Synthetic | XML60000_2126_01           | 60001   | 197  | —             |
| 203  | 🔴 XL   | Synthetic | XML60000_3123_01           | 60001   | 54   | —             |
| 204  | 🔴 XL   | Synthetic | XML60000_3126_01           | 60001   | 197  | —             |
| 205  | 🔴 XL   | Synthetic | XML75000_1173_01           | 75001   | 150  | —             |
| 206  | 🔴 XL   | Synthetic | XML75000_1176_01           | 75001   | 247  | —             |
| 207  | 🔴 XL   | Synthetic | XML75000_2123_01           | 75001   | 45   | —             |
| 208  | 🔴 XL   | Synthetic | XML75000_2173_01           | 75001   | 149  | —             |
| 209  | 🔴 XL   | Synthetic | XML75000_2176_01           | 75001   | 246  | —             |
| 210  | 🔴 XL   | Synthetic | XML80000_1123_01           | 80001   | 54   | —             |
| 211  | 🔴 XL   | Synthetic | XML80000_1126_01           | 80001   | 197  | —             |
| 212  | 🔴 XL   | Synthetic | XML80000_2123_01           | 80001   | 54   | —             |
| 213  | 🔴 XL   | Synthetic | XML80000_2126_01           | 80001   | 197  | —             |
| 214  | 🔴 XL   | Synthetic | XML80000_3123_01           | 80001   | 54   | —             |
| 215  | 🔴 XL   | Synthetic | XML80000_3126_01           | 80001   | 197  | —             |
| 216  | 🔴 XL   | FILO2     | I/Trentino-Alto-Adige     | 100000  | 150  | 102063181.00  |
| 217  | 🔴 XL   | Synthetic | XML100000_1123_01         | 100001  | 45   | —             |
| 218  | 🔴 XL   | Synthetic | XML100000_1173_01         | 100001  | 150  | —             |
| 219  | 🔴 XL   | Synthetic | XML100000_1176_01         | 100001  | 247  | —             |
| 220  | 🔴 XL   | Synthetic | XML100000_2113_01         | 100001  | 8    | —             |
| 221  | 🔴 XL   | Synthetic | XML100000_2121_01         | 100001  | 17   | —             |
| 222  | 🔴 XL   | Synthetic | XML100000_2122_01         | 100001  | 29   | —             |
| 223  | 🔴 XL   | Synthetic | XML100000_2123_01         | 100001  | 45   | —             |
| 224  | 🔴 XL   | Synthetic | XML100000_2124_01         | 100001  | 67   | —             |
| 225  | 🔴 XL   | Synthetic | XML100000_2125_01         | 100001  | 90   | —             |
| 226  | 🔴 XL   | Synthetic | XML100000_2126_01         | 100001  | 142  | —             |
| 227  | 🔴 XL   | Synthetic | XML100000_2133_01         | 100001  | 62   | —             |
| 228  | 🔴 XL   | Synthetic | XML100000_2143_01         | 100001  | 411  | —             |
| 229  | 🔴 XL   | Synthetic | XML100000_2153_01         | 100001  | 610  | —             |
| 230  | 🔴 XL   | Synthetic | XML100000_2163_01         | 100001  | 410  | —             |
| 231  | 🔴 XL   | Synthetic | XML100000_2173_01         | 100001  | 149  | —             |
| 232  | 🔴 XL   | Synthetic | XML100000_2176_01         | 100001  | 246  | —             |
| 233  | 🔴 XL   | Synthetic | XML100000_2223_01         | 100001  | 45   | —             |
| 234  | 🔴 XL   | Synthetic | XML100000_2323_01         | 100001  | 45   | —             |
| 235  | 🔴 XL   | Synthetic | XML100000_3123_01         | 100001  | 45   | —             |
| 236  | 🔴 XL   | Synthetic | XML100000_3126_01         | 100001  | 142  | —             |
| 237  | 🔵 XXL  | FILO2     | I/Basilicata                       | 150000  | 150  | 175623919.00  |
| 238  | 🔵 XXL  | FILO2     | I/Umbria                               | 200000  | 50   | 545507981.00  |
| 239  | 🔵 XXL  | Synthetic | XML200000_2123_01         | 200001  | 54   | —             |
| 240  | 🔵 XXL  | Synthetic | XML200000_2126_01         | 200001  | 197  | —             |
| 241  | 🔵 XXL  | Synthetic | XML200000_3123_01         | 200001  | 54   | —             |
| 242  | 🔵 XXL  | Synthetic | XML200000_3126_01         | 200001  | 197  | —             |
| 243  | 🔵 XXL  | FILO2     | I/Abruzzo                             | 250000  | 200  | 311712556.00  |
| 244  | 🔵 XXL  | FILO2     | I/Friuli-Venezia-Giulia | 300000  | 200  | 415805616.00  |
| 245  | 🔵 XXL  | FILO2     | I/Liguria                             | 320000  | 50   | 1426389867.00 |
| 246  | 🔵 XXL  | FILO2     | I/Calabria                           | 380000  | 50   | 1964651530.00 |
| 247  | 🔵 XXL  | FILO2     | I/Marche                               | 420000  | 200  | 420484426.00  |
| 248  | 🔵 XXL  | FILO2     | I/Sardegna                           | 470000  | 200  | 827934149.00  |
| 249  | 🔵 XXL  | FILO2     | I/Campania                           | 500000  | 200  | 391859276.00  |
| 250  | 🔵 XXL  | Synthetic | XML500000_1173_01         | 500001  | 149  | —             |
| 251  | 🔵 XXL  | Synthetic | XML500000_1176_01         | 500001  | 247  | —             |
| 252  | 🔵 XXL  | Synthetic | XML500000_2123_01         | 500001  | 54   | —             |
| 253  | 🔵 XXL  | Synthetic | XML500000_2126_01         | 500001  | 197  | —             |
| 254  | 🔵 XXL  | Synthetic | XML500000_2173_01         | 500001  | 149  | —             |
| 255  | 🔵 XXL  | Synthetic | XML500000_2176_01         | 500001  | 247  | —             |
| 256  | 🔵 XXL  | Synthetic | XML500000_3123_01         | 500001  | 54   | —             |
| 257  | 🔵 XXL  | Synthetic | XML500000_3126_01         | 500001  | 197  | —             |
| 258  | 🔵 XXL  | FILO2     | I/Piemonte                           | 600000  | 50   | 2627446164.00 |
| 259  | 🔵 XXL  | FILO2     | I/Toscana                             | 700000  | 150  | 1084417188.00 |
| 260  | 🔵 XXL  | Synthetic | XML700000_2123_01         | 700001  | 54   | —             |
| 261  | 🔵 XXL  | Synthetic | XML700000_2126_01         | 700001  | 197  | —             |
| 262  | 🔵 XXL  | Synthetic | XML700000_3123_01         | 700001  | 54   | —             |
| 263  | 🔵 XXL  | Synthetic | XML700000_3126_01         | 700001  | 197  | —             |
| 264  | 🔵 XXL  | FILO2     | I/Puglia                               | 750000  | 200  | 1464797603.00 |
| 265  | 🔵 XXL  | FILO2     | I/Sicilia                             | 800000  | 200  | 1774262462.00 |
| 266  | 🔵 XXL  | FILO2     | I/Veneto                               | 850000  | 200  | 1050488613.00 |
| 267  | 🔵 XXL  | FILO2     | I/Emilia-Romagna               | 900000  | 50   | 5405446715.00 |
| 268  | 🔵 XXL  | FILO2     | I/Lombardia                         | 950000  | 150  | 1339900081.00 |
| 269  | 🔵 XXL  | FILO2     | I/Lazio                                 | 1000000 | 50   | 3145381332.00 |
| 270  | 🔵 XXL  | Synthetic | XML1000000_1173_01       | 1000001 | 149  | —             |
| 271  | 🔵 XXL  | Synthetic | XML1000000_1176_01       | 1000001 | 247  | —             |
| 272  | 🔵 XXL  | Synthetic | XML1000000_2123_01       | 1000001 | 45   | —             |
| 273  | 🔵 XXL  | Synthetic | XML1000000_2126_01       | 1000001 | 142  | —             |
| 274  | 🔵 XXL  | Synthetic | XML1000000_2173_01       | 1000001 | 149  | —             |
| 275  | 🔵 XXL  | Synthetic | XML1000000_2176_01       | 1000001 | 247  | —             |
| 276  | 🔵 XXL  | Synthetic | XML1000000_3123_01       | 1000001 | 45   | —             |
| 277  | 🔵 XXL  | Synthetic | XML1000000_3126_01       | 1000001 | 142  | —             |
| 278  | 🟤 XXXL | Synthetic | XML1500000_1173_01       | 1500001 | 149  | —             |
| 279  | 🟤 XXXL | Synthetic | XML1500000_1176_01       | 1500001 | 247  | —             |
| 280  | 🟤 XXXL | Synthetic | XML2000000_1113_01       | 2000001 | 8    | —             |
| 281  | 🟤 XXXL | Synthetic | XML2000000_1121_01       | 2000001 | 17   | —             |
| 282  | 🟤 XXXL | Synthetic | XML2000000_1123_01       | 2000001 | 45   | —             |
| 283  | 🟤 XXXL | Synthetic | XML2000000_1126_01       | 2000001 | 142  | —             |
| 284  | 🟤 XXXL | Synthetic | XML2000000_1173_01       | 2000001 | 149  | —             |
| 285  | 🟤 XXXL | Synthetic | XML2000000_1176_01       | 2000001 | 247  | —             |
| 286  | 🟤 XXXL | Synthetic | XML2000000_2113_01       | 2000001 | 8    | —             |
| 287  | 🟤 XXXL | Synthetic | XML2000000_2121_01       | 2000001 | 17   | —             |
| 288  | 🟤 XXXL | Synthetic | XML2000000_2122_01       | 2000001 | 29   | —             |
| 289  | 🟤 XXXL | Synthetic | XML2000000_2123_01       | 2000001 | 45   | —             |
| 290  | 🟤 XXXL | Synthetic | XML2000000_2124_01       | 2000001 | 67   | —             |
| 291  | 🟤 XXXL | Synthetic | XML2000000_2125_01       | 2000001 | 90   | —             |
| 292  | 🟤 XXXL | Synthetic | XML2000000_2126_01       | 2000001 | 142  | —             |
| 293  | 🟤 XXXL | Synthetic | XML2000000_2133_01       | 2000001 | 61   | —             |
| 294  | 🟤 XXXL | Synthetic | XML2000000_2143_01       | 2000001 | 411  | —             |
| 295  | 🟤 XXXL | Synthetic | XML2000000_2153_01       | 2000001 | 610  | —             |
| 296  | 🟤 XXXL | Synthetic | XML2000000_2163_01       | 2000001 | 411  | —             |
| 297  | 🟤 XXXL | Synthetic | XML2000000_2173_01       | 2000001 | 149  | —             |
| 298  | 🟤 XXXL | Synthetic | XML2000000_2176_01       | 2000001 | 247  | —             |
| 299  | 🟤 XXXL | Synthetic | XML2000000_2223_01       | 2000001 | 45   | —             |
| 300  | 🟤 XXXL | Synthetic | XML2000000_2323_01       | 2000001 | 45   | —             |
| 301  | 🟤 XXXL | Synthetic | XML2000000_3113_01       | 2000001 | 8    | —             |
| 302  | 🟤 XXXL | Synthetic | XML2000000_3121_01       | 2000001 | 17   | —             |
| 303  | 🟤 XXXL | Synthetic | XML2000000_3123_01       | 2000001 | 45   | —             |
| 304  | 🟤 XXXL | Synthetic | XML2000000_3126_01       | 2000001 | 142  | —             |
| 305  | 🟤 XXXL | Synthetic | XML2000000_3161_01       | 2000001 | 155  | —             |
| 306  | 🟤 XXXL | Synthetic | XML2000000_3173_01       | 2000001 | 149  | —             |
| 307  | 🟤 XXXL | Synthetic | XML2000000_3176_01       | 2000001 | 247  | —             |
| 308  | 🟤 XXXL | Synthetic | XML5000000_1176_01       | 5000001 | 247  | —             |
| 309  | 🟤 XXXL | Synthetic | XML5000000_2173_01       | 5000001 | 150  | —             |
| 310  | 🟤 XXXL | Synthetic | XML5000000_2176_01       | 5000001 | 247  | —             |




---



## CVRPLIB

Standard capacity-only CVRP benchmarks from [CVRPLIB](http://vrp.atd-lab.inf.puc-rio.br/index.php/en/) *(accessed 15 April 2026)*.

- Layout: TSPLIB `.vrp`
- Edge weights: `EUC_2D`
- Constraint: vehicle capacity `Q` only
- Count: **130** instances


| Set        | #   | Source                                                                   |
| ---------- | --- | ------------------------------------------------------------------------ |
| **CMT**    | 1   | Christofides, Mingozzi & Toth (CMT5 only)                                |
| **E**      | 4   | Christofides & Eilon                                                     |
| **F**      | 1   | Fisher                                                                   |
| **P**      | 1   | Augerat et al.                                                           |
| **Golden** | 12  | Golden et al. (Golden_9–20)                                              |
| **X**      | 100 | Uchoa et al.                                                             |
| **tai**    | 1   | Taillard                                                                 |
| **AGS**    | 10  | Arnold, Gendreau & Sörensen (Antwerp, Brussels, Flanders, Ghent, Leuven) |




### Exclusions

Distance- / service-constrained variants, and CMT instances outside this benchmark, are not kept:

- `Golden_1`–`Golden_8` — `DISTANCE`
- `CMT1`–`CMT4`, `CMT11`–`CMT12` — capacity-only but not in this benchmark set
- `CMT6`–`CMT10`, `CMT13`–`CMT14` — `DISTANCE` + `SERVICE_TIME`
- **Li** set — every instance has `DISTANCE`

---



## FILO2

Large-scale Italian regional instances under `FILO2/I/` *(accessed 15 April 2026)*.

- Layout: TSPLIB `.vrp` (BKS costs from the paper; no `.sol` routes bundled here)
- Edge weights: `EUC_2D`
- Constraint: vehicle capacity `Q`
- Scale: **L** / **XL** / **XXL** (~20k – 1M customers)
- Count: **20** instances

**Reference:** L. Accorsi & D. Vigo, *A fast and scalable heuristic for the solution of large-scale capacitated vehicle routing problems*, Computers & Operations Research, 2024. [doi:10.1016/j.cor.2024.106562](https://dl.acm.org/doi/10.1016/j.cor.2024.106562)

---



## Synthetic

XML-style synthetic CVRP instances under `Synthetic/`, generated with the Uchoa et al. generator.

- Layout: TSPLIB `.vrp` (no BKS / `.sol` bundled)
- Edge weights: `EUC_2D`
- Constraint: vehicle capacity `Q`
- Count: **160** instances
- Scale: **XS** – **XXXL** (10 – 5,000,000 customers)



### Naming

`XML<n>_<depotPos><custPos><demandType><avgRouteSize>_<instanceID>.vrp`


| Field                | Values                                                                                            |
| -------------------- | ------------------------------------------------------------------------------------------------- |
| `n`                  | Number of customers                                                                               |
| Depot positioning    | `1` Random · `2` Centered · `3` Cornered                                                          |
| Customer positioning | `1` Random · `2` Clustered · `3` Random-clustered                                                 |
| Demand distribution  | `1` Unitary · `2`–`5` small/large ± variance · `6` quadrant-dependent · `7` few large, many small |
| Average route size   | `1` Very short · `2` Short · `3` Medium · `4` Long · `5` Very long · `6` Ultra long               |
| `instanceID`         | Instance index (here `01`)                                                                        |


**References:** Uchoa et al. (2017), *New benchmark instances for the Capacitated Vehicle Routing Problem*, EJOR. Queiroga et al. (2022), *10,000 optimal CVRP solutions for testing machine learning based heuristics*.

---



## Sample

Tiny hand-written instances for quick local checks (not part of the benchmark counts above):

- [Sample/eg](Sample/eg.vrp) — `N=7`, `Q=5`
- [Sample/toy](Sample/toy.vrp) — `N=6`, `Q=30`

