# aws-iot-mqtt

Cloud & Devops Master - PROJECT WORK
Proge;are e configurare un’archite;ura cloud per il monitoraggio e
controllo di impianC industriali
ObieEvo
L'obieEvo di questo project work è quello di proge;are, e successivamente configurare,
un'infrastru;ura Cloud Amazon Web Services (AWS) per conto di un’azienda produ;rice di
impianC di deumidificazione che desidera monitorare in tempo reale i daC provenienC dalle
schede dei loro impianC. Allo stesso tempo dovrà essere possibile inviare comandi per la
gesCone dell’impianto da remoto. L'azienda desidera creare un sistema che consenta alle
schede dei disposiCvi di conne;ersi ad un gateway che raccolga i daC dai sensori in tempo
reale e li invii al cloud AWS per l'elaborazione e la visualizzazione.
Descrizione del Project Work
In questo Project Work, il team dovrà immaginare di affiancare il cliente nelle diverse aEvità
chiave al fine di proge;are un'infrastru;ura nel cloud AWS, per supportare l'intero flusso dei
daC dalla raccolta, visualizzazione e invio comandi da remoto.
Si chiede di seguire un approccio completo che includa la proge;azione dell'archite;ura,
l’oEmizzazione dei daC da inviare e meccanismi di allarme in tempo reale.
I vincoli della proge;azione sono:
- proge;are un'archite;ura scalabile ed efficiente che consenta la connessione delle
schede dei disposiCvi al gateway esterno, l'invio e la ricezione dei daC in cloud AWS
- sicurezza dei protocolli di comunicazione
- affidabilità delle connessioni
- il costo a macchina per i servizi cloud non deve superare € 0,50 / anno
Il team potrà scegliere i servizi AWS che riCene più adeguaC all’o;enimento del risultato.
Successivamente, bisognerà studiare una tecnica per oEmizzare al massimo la dimensione
dei daC da inviare in cloud, per evitare duplicazioni di informazioni, ma pensando anche che
dovranno essere facilmente interrogabili da API o query SQL.
Le schede prevedono diversi Cpi di variabili, che cambiano in base alla Cpologia di macchina.
Ogni variabile è idenCficata da un codice univoco (indirizzo MODBUS).
Un Cpo di variabile che le schede producono sono gli allarmi: errori o guasC nella macchina.
Sono gli stessi per tu;e le macchine: un insieme di allarmi di esempio è il seguente.
Codice Descrizione Tipologia
500 allarme generico boolean
501 allarme sonde macchina boolean
502 allarmi ingressi boolean
503 allarmi da logiche boolean
504 allarmi circuito frigo 1 boolean

505 allarmi circuito frigo 2 boolean
506 allarmi rese;abili boolean
507 allarmi non rese;abili boolean
550 guasto sonda CO2 ambiente boolean
551 guasto sonda VOC ambiente boolean
552 guasto sonda temperatura ambiente boolean
553 guasto sonda temperatura esterna boolean
554 guasto sonda temperatura acqua boolean
555 guasto sonda temperatura mandata boolean
556 guasto sonda temperatura protezione anCgelo ba; acqua boolean
557 guasto sonda temperatura sbrinamento recuperatore boolean
558 guasto sonda umidità ambiente boolean
600 allarme resistenze ele;riche grave boolean
601 allarme resistenze ele;riche lieve boolean
602 allarme fuga gas boolean
603 allarme venClazione boolean
604 allarme venClatore ricircolo boolean
605 allarme venClatore estrazione boolean
606 allarme venClatore condensazione boolean
607 allame flussostato grave boolean
608 allarme flussostato lieve boolean
609 allarme sequenza fasi boolean
650 segnalazione pulire filtri boolean
651 segnalazione pulire tubo ionizzatore boolean
652 segnalazione sosCtuire tubo ionizzatore boolean
653 allarme protezione anCgelo ba;eria acqua boolean
654 allarme protezione ba;eria acqua lieve boolean
655 allarme alta temperatura acqua per on compressore boolean
656 allarme bassa temperatura per on compressore boolean
657 allarme anCgelo ba;eria acqua kit controllo temperatura mandata grave boolean
658 allarme anCgelo ba;eria acqua kit controllo temperatura mandata lieve boolean
659 allarme macchina scarica boolean
660 allarme mancanza comunicazione con display boolean
661 allarme mancanza comunicazione con ionizzatore boolean
662 allarme mancanza comunicazione modbus master boolean
Un'altra Cpologia di variabili sono le variabili binarie: ogni Cpologia di macchine ha le proprie
variabili, mappate in modalità differenC. Degli esempi di variabili possono essere i seguenC.
Notare che il codice della variabile è univoco solo all’interno di una Cpologia di macchina.
Tipologia A
Codice Descrizione Tipologia
1 On / Off boolean
2 On effeEvo boolean
3 Stagione boolean
4 Stagione effeEva boolean
5 Abilitazione fasce orarie su display macchina boolean
6 Deumidifica aEva boolean
7 Richiesta acqua per tra;amento aria boolean
8 Warning filtri sporchi boolean
9 Allarme generico boolean
10 Reset allarmi boolean

11 Abilitazione deumidifica boolean
12 Abilitazione riscaldamento boolean
13 Abilitazione raffreddamento boolean
14 Abilitazione free-cooling\heaCng boolean
15 Presenza riscaldamento dell’aria boolean
16 Presenza raffreddamento dell’aria boolean
17 Presenza recuperatore boolean
18 Presenza free-cooling\heaCng boolean
19 Riscaldamento aEvo boolean
20 Raffreddamento aEvo boolean
21 Ricambio aEvo boolean
22 Free-cooling\heaCng aEvo boolean
23 Sbrinamento aEvo boolean
24 Abilitazione riduzione venClazione boolean
25 Abilitazione umidifica boolean
26 Sbrinamento recuperatore aEvo boolean
27 Presenza condensatore remoto boolean
28 Presenza valvola acqua boolean
29 Presenza valvola acqua on-off boolean
30 Presenza valvola acqua modulante boolean
31 Presenza e abilitazione ba;eria acqua calda boolean
32 Presenza e abilitazione ba;eria acqua fredda boolean
33 Presenza controllo temperatura boolean
34 On compressore 1 boolean
35 On compressore 2 boolean
36 On venClatore mandata boolean
37 On resistenza ele;riche boolean
Tipologia B
Codice Descrizione Tipologia
1 Unità ON boolean
2 Forzatura deumidifica boolean
3 Abilitazione forzatura deumidifica [1] boolean
4 Forzatura riscaldamento [2] boolean
5 Abilitazione forzatura riscaldamento [1] boolean
6 Reset allarmi boolean
7 Reset pulizia filtri boolean
8 Forzatura raffreddamento [2] boolean
9 Abilitazione forzatura raffreddamento [1] boolean
10 Stato compressore boolean
11 Stato valvola acqua boolean
12 Stato resistenza ele;rica boolean
13 Presenza valvola acqua boolean
14 Presenza resistenza ele;rica boolean
15 Presenza allarme boolean
16 Filtri da pulire boolean
17 Presenza venClatori ele;ronici boolean
18 Presenza opzione sbrinamento gas caldo boolean
19 Allarme sonda boolean
20 Allarme alta pressione boolean
21 Allarme bassa pressione boolean
22 Allarme macchina scarica boolean
23 Allarme bassa temperatura per ON compressore boolean

24 Allarme sovratemperatura resistenza ele;rica boolean
25 Allarme sovratemperatura resistenza ele;rica boolean
26 Allarme venClatore boolean
27 Sbrinamento aEvo boolean
28 Richiesta deumidifica boolean
29 Richiesta riscaldamento boolean
30 Richiesta raffreddamento boolean
Le macchine producono anche variabili analogiche (solamente interi e decimali): anche queste
disCnte in base alla Cpologia.
Tipologia A
Codice Descrizione Tipologia
1 temperatura ambiente float
2 temperatura esterna float
3 umidità relaCva ambiente float
4 set umidità relaCva float
5 set umidità relaCva effeEva float
6 set temperatura / set temperatura inverno float
7 set temperatura estate float
8 set temperatura effeEvo float
9 Percentuale venClatore mandata integer
10 Percentuale venClatore estrazione integer
11 Percentuale valvola acqua integer
12 Percentuale umidificatore integer
13 Percentuale valvola gas integer
14 Percentuale serranda free-cooling integer
15 Percentuale serranda ricircolo integer
16 Set sbrinamento staCco float
17 Differenziale sbrinamento staCco float
18 Tempo sgocciolamento sbrinamento staCco integer
19 Temperatura mandata in ambiente integer
20 Versione sorware float
21 Percentuale ricambio, step fisso e minimo di 5% integer
22 Percentuale ricambio effeEvo integer
23 Temperatura protezione ba;eria acqua float
24 Temperatura ingresso ba;eria acqua float
25 temperatura ambiente float
Tipologia B
Codice Descrizione Tipologia
1 Forzatura umidifica integer
2 Set temperatura float
3 Set umidità relaCva float
4 Ventilatore di ricircolo in standby (1 == Off, 2 == Minima, 3 === Nominale) integer
5 Differenziale on raffreddamento float
6 Differenziale off raffreddamento float
7 Differenziale on deumidifica float
8 Differenziale off deumidifica float
9 Differenziale on riscaldamento float
10 Differenziale off riscaldamento float
11 Inizio rampa umidifica float

12 Fine rampa umidifica float
13 Offset temperatura ambiente float
14 Offset umidità ambiente float
15 Ore di a;esa promemoria pulizia filtri integer
16 Taratura fase 1 – venClatore mandata integer
17 Taratura fase 2 – venClatore mandata integer
18 Taratura fase 2 – venClatore estrazione integer
19 Taratura fase 3 – venClatore mandata integer
20 Taratura fase 3 – serranda ricircolo integer
21 Taratura fase 1 – venClatore mandata integer
22 Taratura fase 2 – venClatore mandata integer
23 Taratura fase 2 – venClatore estrazione integer
24 Taratura fase 3 – venClatore mandata integer
25 Taratura fase 3 – serranda ricircolo integer
È importante quindi organizzare i daC in una stru;ura applicabile a tu;e le macchine e che sia
resistente a future aggiunte di nuove variabili o macchine, in modo da poter inviare tuE i daC
necessari tramite MQTT in formato binario, numerico e/o stringa.
Infine, è richiesto di proge;are meccanismi di allarme in tempo reale che segnalino eventuali
anomalie o condizioni criCche. Questo consenCrà all'azienda di essere prontamente informata
di qualsiasi situazione che richieda un intervento immediato. Sfru;ate i servizi di monitoraggio
e allarme di AWS per implementare questa funzionalità.
L’aspe;o più importante di questo project work è l'inclusione dei cosC dell'infrastru;ura e del
servizio nel costo delle macchine di deumidificazione. Ciò significa che è richiesto di tenere i
cosC dell’infrastru;ura più bassi possibile.
È richiesto di calcolare e presentare i cosC associaC all'infrastru;ura implementata, in modo
che l'azienda possa includerli nel prezzo finale delle loro macchine.
Ricordiamo che l’intera proge;azione dovrà essere svolta secondo le best pracCce di AWS per
quanto riguarda la sicurezza, la scalabilità e l'oEmizzazione dei cosC durante l'intero processo.

Output a;esi
Il team dovrà consegnare la seguente documentazione:
- Documento di proge;o con assunzioni fa;e per la realizzazione della proposta fa;a e
calculator dei cosC teorici di infrastru;ura
- Template CDK dell’archite;ura
- Codice sorgente degli script scriE per simulare un impianto
- Screenshot cost explorer dei cosC di infrastru;ura reali e confronto con il calcolo
teorico mappando eventuali azioni di miglioramento
