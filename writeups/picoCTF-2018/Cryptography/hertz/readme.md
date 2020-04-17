# hertz

__PROBLEM__

 Here's another simple cipher for you where we made a bunch of substitutions. Can you decrypt it? Connect with nc 2018shell1.picoctf.com 43324.

__HINT__

NOTE: Flag is not in the usual flag format

__SOLUTION__

We connect to the given port and we are greeted by:
```
-------------------------------------------------------------------------------
aldukhpe wrkr qe ylxk jbhu - exoepqpxpqld_aqswrke_hkr_elbchobr_ctheakvqhz
-------------------------------------------------------------------------------
ephprby, sbxzs oxag zxbbquhd ahzr jklz pwr ephqkwrht, orhkqdu h olvb lj
bhpwrk ld vwqaw h zqkklk hdt h khflk bhy akleert. h yrbblv tkreeqduulvd,
xduqktbrt, vhe exephqdrt urdpby orwqdt wqz ld pwr zqbt zlkdqdu hqk. wr
wrbt pwr olvb hbljp hdt qdpldrt:

-qdpklqol ht hbphkr trq.

whbprt, wr srrkrt tlvd pwr thkg vqdtqdu ephqke hdt ahbbrt lxp alhkerby:

-alzr xs, gqdaw! alzr xs, ylx jrhkjxb mrexqp!

elbrzdby wr ahzr jlkvhkt hdt zlxdprt pwr klxdt uxdkrep. wr jhart holxp
hdt obreert ukhcrby pwkqar pwr plvrk, pwr exkklxdtqdu bhdt hdt pwr
hvhgqdu zlxdphqde. pwrd, ahpawqdu equwp lj eprswrd trthbxe, wr ordp
plvhkte wqz hdt zhtr khsqt akleere qd pwr hqk, uxkubqdu qd wqe pwklhp
hdt ewhgqdu wqe wrht. eprswrd trthbxe, tqesbrhert hdt ebrrsy, brhdrt
wqe hkze ld pwr pls lj pwr ephqkaher hdt bllgrt albtby hp pwr ewhgqdu
uxkubqdu jhar pwhp obreert wqz, rnxqdr qd qpe brdupw, hdt hp pwr bquwp
xdpldexkrt whqk, ukhqdrt hdt wxrt bqgr shbr lhg.

oxag zxbbquhd srrsrt hd qdephdp xdtrk pwr zqkklk hdt pwrd alcrkrt pwr
olvb ezhkpby.

-ohag pl ohkkhage! wr ehqt eprkdby.

wr httrt qd h skrhawrke pldr:

-jlk pwqe, l trhkby orblcrt, qe pwr urdxqdr awkqepqdr: olty hdt elxb
hdt obllt hdt lxde. eblv zxeqa, sbrher. ewxp ylxk ryre, urdpe. ldr
zlzrdp. h bqppbr pklxobr holxp pwler vwqpr alksxeabre. eqbrdar, hbb.

wr srrkrt eqtrvhye xs hdt uhcr h bldu eblv vwqepbr lj ahbb, pwrd shxert
hvwqbr qd khsp hpprdpqld, wqe rcrd vwqpr prrpw ubqeprdqdu wrkr hdt pwrkr
vqpw ulbt slqdpe. awkyeleplzle. pvl epkldu ewkqbb vwqepbre hdevrkrt
pwklxuw pwr ahbz.

-pwhdge, lbt awhs, wr akqrt okqegby. pwhp vqbb tl dqarby. evqpaw ljj
pwr axkkrdp, vqbb ylx?

wr egqssrt ljj pwr uxdkrep hdt bllgrt ukhcrby hp wqe vhpawrk, uhpwrkqdu
holxp wqe brue pwr bller jlbte lj wqe ulvd. pwr sbxzs ewhtlvrt jhar hdt
exbbrd lchb mlvb krahbbrt h skrbhpr, shpkld lj hkpe qd pwr zqttbr hure.
h sbrhehdp ezqbr oklgr nxqrpby lcrk wqe bqse.
```
And using the [solver](https://www.guballa.de/substitution-solver) we get the flag:

FLAG - `picoCTF{substitution_ciphers_are_solvable_vdascrwiam}`
