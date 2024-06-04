from sentence_transformers import SentenceTransformer
import torch

# Load model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

sentence1 = "ఓం శనీశ్వరాయ నమః ఓం శని గ్రహ నమః ఓం శనీశ్వరాయ నమః ఓం శ్రీ కరాయ నమః ఓం శనిగ్రహ నమః ఓం యానికానిచ పాపాని ఓం శనీశ్వరాయ నమః ఇంకో 20 20 ఏంటి సార్ అంతలో వెతుకుతున్నారు 25 పైసలు కోసం సార్ లేనట్టు ఉంది మీ దగ్గర కూడా చెల్లెలు లేదా ఫోన్ లేదు సార్ పాల కోసం చూసుకోలేదు రేపు వచ్చినప్పుడు ఆ పాలు ఇచ్చేస్తాను పాముల కోసం సారీ ఎందుకు వేస్ట్ చేసుకుంటారు ఈ ప్రపంచంలోనే ఉండాలని అనుకుంటున్నా నీలో జాగ్రత్త లోపించింది ప్రతి నయా పైసా ఎంత విలువైందో నీకు అసలు తెలియటం లేదు ఒక్క పావలాకి రూపాయి పావలా తిట్లు తిట్టలేదు లేరా ఒక్కో నీటి బొట్టు కలిస్తేనే మహా సముద్రం రా ఒక్కో పావలా కలిస్తేనే బాటలో రూపాయలు అంటే నేను పావురాలు రూపంలో కోట్ల రూపాయలు నష్టం తీసుకోవడం వల్ల బిజినెస్ డెవలప్మెంట్ లేదన్నారు కాలిక్యులేట్ చేసిన కోటి 70 లక్షల పైన అవుతుంది చూడు చూసావా క్యాలిక్యులేటర్ లో కూడా పెట్టట్లేదు చూసావా ఇన్ఫినిటీ అంతే అనంతం అంత అమౌంట్ మనం నష్టపోతున్నాం అన్నమాట ఏంటో నాకు అన్ని సినిమాల్లో కనపడుతున్నాయి సార్ వాడు నీ బుర్రంతా శూన్యం కాబట్టి అలాగే కనపడుతుంది ఇప్పటికైనా కళ్లు తెరిచి మనకు జరిగిన నష్టాన్ని భర్తీ చేసుకోవాల్సిన బాధ్యత మన మీద ఎంతైనా ఉంది తెలుసా అంటే వాస్తు గ్రహస్థితి ఓహో రీసెంట్గా భూమికి సూర్యుడికి మధ్యలో శనిగ్రహం ప్రవేశించింది తెలుసా వాడు శనిగ్రహం అంటే పురాణాల ప్రకారం సాక్షాత్తు శనీశ్వరుడు శని ప్రభావం ఉండకుండా ఈ అమావాస్య వెళ్లే వరకు మన హోటల్ ని కాంతులు ధగధగలు తో మెరిసిపోయేలా చెయ్యాలి నువ్వు మాత్రం కూడా వదలకుండా ముక్కు పిండి వసూలు చేయాలి ఈరోజు నుంచి మనం డబ్బు విషయంలో చాలా స్ట్రిక్ట్ అని అందరికీ తెలియాలి ఓకే రా ఈరోజు నుంచి కొత్త అమృతాన్ని చూస్తావు రెండు ప్లేట్లు పెసరట్టు సరోవర రెండు ప్లేట్లు టిఫిన్ బాగుంది సార్ 20 అయ్యో వర్షం మర్చిపోయాను అండి ఏంటి సార్ పర్సనల్ హాయ్ సార్ ఏం చేస్తున్నావ్ సార్ ఇలా పర్సనల్ చచ్చిపోయినప్పుడు ఏ ప్రాబ్లం రాకుండా ఉండటానికి డబ్బులు సీక్రెట్ ప్లేస్ లో పెట్టుకుంటారు సార్ అదే వెతుకుతున్న నాటకాలు వస్తున్నావా మానేశారు సార్ ఇప్పుడు టీవీలో కొత్త అందుకే హైదరాబాద్ వచ్చాను కానీ దాంట్లో వర్షం ఎంత మాట అనేసారు మీ డబ్బులు సాయంత్రం తెచ్చిస్తారు సార్ సాయంత్రం తీసుకొచ్చి ఇస్తా రేపు పొద్దున్నే తీసుకొచ్చి ఇస్తా ఇలాంటి కాకమ్మ కబుర్లు చాలా ఉన్నావమ్మా పోనీ ఒక గంట తెచ్చి ఇచ్చాడా అరగంట చాలు కదా సిటీ తట్టుకోవడం కోసం పది రూపాయల కోసం జరుగుతుంది మీకు ఎలా చెప్పాలి కొడతారా నేను ఎందుకు చేస్తాను మీ చేత లేబర్ వర్క్ చేయిస్తా నాకు తెలుసా ఎవరైనా నేర్పిస్తారా సర్వం చూడకపోతే ఓనర్ లో ఉన్నాను సార్ మనకి 20 రూపాయలు బాకీ పడ్డారు రా లోపలికి తీసుకెళ్తుంది ఇంటికి ఏంటి ఇప్పుడు ఇదంతా రూపాలే అవునులే వీడి పిండి ఇప్పుడు ఎంత వరకు వచ్చింది బాబు ఏం చేస్తున్నావ్ ఇలా ఎన్ని రోజులు తిరిగి కూడా చెప్పాడు ఇలా తిరుగుతున్నాడు బాబు వచ్చేస్తుంది సార్ ఐదు నిమిషాలు ఒరేయ్ ఇవాళ ఇల్లు మనకు దోశ పెట్టగానే ఏంట్రా సప్లై లేటవుతుంది కస్టమర్స్ వెయిట్ చేసి వెళ్ళిపోతున్నారు ఏమైంది ఏం జరుగుతుంది అక్కడ పది మంది దోస్త్ కస్టమర్లు విసిగిపోయి వెళ్ళిపోయారు లేదా ఒక చాలు కానీ తీసుకొచ్చి ఇక్కడ పెట్టమని ఇప్పటికైనా తీసుకొచ్చాడు రా ఏంటిది పిండి మంచిగా అయితే కొంచెం పిండి కలిపాను ఆయన ఉంది కొంచెం కొంచెం నీళ్లు కలిపి కొట్టుకుంటున్నారు నేను ముందే చెప్పాను కదా అని నాకు ఇలాంటి పనులు రావని సరే నీకు వచ్చే పనులు చేపిస్తా టిఫిన్ చేసేసాను అండి ప్లేట్లు కొడుకు ఎవరు అండి వాణి సాంస్క్రిట్ మూటగట్టి బట్టలు ఉతికి ఒక్క నిమిషంలో అయిపోతాయి అని జోక్ చేశా వార్తలు ఎక్కడ ఉందో ఆరోగ్యం ఎక్కడ ఉంది తప్పు మీద తప్పు మీద నష్టం చాలా కష్టం నేను పోతా ఎక్కడికి పోయేది చ చ సర్వో ఒరేయ్ సర్వో వాడు అసలు కోపం చూడు ఎవరు మనం ఉంటారా ఏంటి ఏరా దీన్ని బట్టి నీకు అర్థం అయిందా ఏంటి కొడితే బాగుండు అనిపిస్తుంది ఇందులో నా ఉద్దేశ్యం ఏంటంటే ఈ ఒక్క పనులను వాడు చెడగొట్టడానికి అంటే ఏమి ఉండదు అమ్మయ్య ఇప్పటికే కింది వాటర్ ఇదేంటి అన్నయ్య శర్మ ఏంటి సార్ వాడు చూడు ఇక్కడ సరిగ్గా రావట్లేదు ఐదు నిమిషాలు ఆగండి నాలుగైదు బకెట్లో పోస్తే కానీ అందం వేయకుండా కరెంట్ సేవ్ చేయడానికి అమృతం సార్ వాడు ఆ బిల్డింగ్ కస్టమర్ తోటి బట్టలతో నీళ్లు పోస్తారు పైకి చిన్న అన్ని ఇక్కడ బాత్రూం లో పెట్టి పైన వాటర్ పోషిస్తున్నారు మీ తెలుగు తగలడు నామీద ఇది కరెక్ట్ కాదు రా బాబు ఏంట్రా వాటర్ ఇక్కడ పెట్టావా ఇక్కడ కాదు బకెట్ పాలు పాలు డాక్టర్ కాలు టాక్ టు కాల్ ఒరేయ్ అమృతం నయా పైసా కూడా జారిపోకుండా జాగ్రత్త పడాలని చెప్పినందుకు ఎంత పని చేశారు నుంచి జరిగిన నష్టాన్ని కాలిక్యులేట్ చేస్తే గాని వాటి గురించి నేను కంక్లూషన్ రాలేను ఆ క్యాలిక్యులేటర్ ఇవ్వు అన్న మినప్పప్పు 7 కిలోలు 7 కిలోలు అంటే 7 * 29 ఇదిలాగే అయినా సరే రికవరీ చేయాలి నాకు ఓవరాల్ గా ఎంత అవుతుంది అని కాదు విడివిడిగా ఎంత ఉందో చెప్పండి చెక్ చేస్తుంటే సరిపోద్ది ఓకే టైమర్ క్యాన్సిల్ కంటిన్యూగా ఒక మనిషి లేకపోతే ప్రాబ్లం అవుద్ది అని నేను చూసుకుంటా సరే ఒక 10000 డిపాజిట్ ఇవ్వండి తీస్కో మా హోటల్ బిజినెస్ గా వెళ్లడం కోసం మంచి లైటింగ్ ఏర్పాటు చేశారు దేనికి కదలకుండా ఏదన్నా సక్రమంగా చెయ్ ఏం చేయాలి పొద్దున పిండి పాడు చేసినప్పుడే పంపించండి నా కర్మ ఒరేయ్ ఇంకా ఏం మొహం పెట్టుకుని ఇక్కడ నా గురించి వంటవాడు ఇక్కడి నుంచి కథలు వద్దండి నువ్వు చేసిన పని ఇంకా సరిపోలేదట అడిగారు సర్ దీన్ని కూడా చదవండి అన్నారుగా ఒక మంచి డెసిషన్ తీసుకున్న అసలు ఈ దేశం పొద్దున తీసుకుంటే బాగుండేది సర్లే ఏమైతది దాని నెంబర్ శనిగ్రహం వాడు కాదు రా నువ్వు ఏవండీ పొద్దున అన్ని చేపలు ఎత్తుకున్న గాని పై చేయి వెతుక్కోవాలి డబ్బులు దీంట్లోనే ఉన్నాయండి తీసుకోండి శనీశ్వరాయ నమః గోరె గుడ్డలు అయితే"
sentence2 = "సార్ వాడు ఈ అల్పాహారం టేస్ట్ చేయండి కదా చెప్పండి ఇంతవరకు సరోవరం నాకు తెలుగు మాటలు నేర్పించలేదు మీరు కొంచెం టెస్ట్ చేయండి ఎక్స్పీరియన్స్ లేకపోయినా ఎక్స్పరిమెంట్స్ కి తక్కువ లేదు మళ్లీ మీకు వినిపిస్తోంది కొంచెం ఎక్కువ అయినదా చాలా కరెక్ట్గా చేస్తున్నావ్ ఎలా బాగా చేస్తుంటారు వాడు ఇంకొంచెం బూందీ తయారు చేసి ఇందులో కలుపుతారు ఎలా తయారయ్యావ్ లేదురా వాడు పిచ్చి ప్రయోగం చేస్తున్నాడు అని చిన్న కోపం వచ్చింది అంతే గుడ్ మార్నింగ్ సార్ గుడ్ మార్నింగ్ ఎవరు కావాలి సార్ నేను డాక్టర్స్ డయాగ్నస్టిక్ సెంటర్ మీతో మాట్లాడుతాను మీరు ఎప్పుడైనా టోటల్ బాడీ హెల్త్ చెకప్ చేయించుకున్నారా సార్ మీకు చేయించుకునే ఉద్దేశం ఉంటే మా హాస్పిటల్ కి రండి ఖర్చులు 50% డిస్కౌంట్ మీరు 2000 కట్టి హెల్త్ కార్డు తీసుకుంటే మీకు మూడు నెలల పాటు టెస్టులు అదే పొరపాటు మనం పైకి ఎంత ఆరోగ్యంగా కనిపించినా లోపల మనకు తెలియని ఎన్నో ఉన్నాయి ఈ రోజుల్లో వయసుతో సంబంధం లేకుండా బిపి షుగర్ హాట్ కంప్లైంట్స్ లాంటి వస్తున్నాయి సార్ ముందు జాగ్రత్తగా ఇలాంటి టెస్ట్ లన్ని చేయించుకుంటే అన్ని కంట్రోల్ ఉంచుకోవచ్చు మనం ఎలాగూ హెల్త్ చెకప్ లాంటివి చేయించుకోవాలి ఇలాంటి స్కీములు 50% డిస్కౌంట్ ఉన్నప్పుడు మాత్రమే చేయించుకోవాలి ఏ సింటమ్స్ లేనప్పుడు మనకు అనవసరంగా ఈ ఖర్చు ఎందుకు అంటున్న సింటమ్స్ తెలిస్తే అప్పుడు బాబు నీకు అర్థం కావట్లా ఇప్పుడు నువ్వు లావుగా కనిపిస్తున్నావు అదంతా ఆరోగ్యం అందం బలం బొద్దుగా ముద్దుగా కనిపిస్తున్నారు నీ ఫీలింగ్ అదంతా కొలవలేని కొలెస్ట్రా అంటే కొవ్వా అదే ఎక్కువైతే హార్ట్ ప్రాబ్లమ్స్ వస్తాయి మీకు ఉపయోగకరంగా ఉంటుంది ఆలోచించండి సార్ మనసులో ఒక గిన్నె వచ్చి చేరాక అది క్లారిఫై చేసుకునేదాకా కుదురుగా ఉండడం సరే ఆ స్కీమ్ లో మేము జాయిన్ అవుతాను అప్లికేషన్ ఫిల్ చేయనా ఒరేయ్ అరవం లంచ్ పెట్టరా సార్ ఇక్కడ సైన్ చేయండి అది సమయానికి వచ్చారు సార్ మీరు స్క్రీన్ లో చేరండి స్కీమ్లో హెల్త్ చెకప్ కి 50% డిస్కౌంట్ స్కీమ్ పెట్టారు 2000 కి మూడు నెలల పాటు అన్ని టెస్టులు ఫ్రీగా ఇది మీ హెల్త్ కార్డు ఇది మీ కార్డు తీసుకురావాలని కంపల్సరిగా తీసుకొస్తే మంచిది సార్ ఒకవేళ మర్చిపోయిన ఇది మీ కోడ్ నెంబర్ 331 332 ఈ కోడ్ నెంబర్ చెప్పు మీరు అన్ని టెస్టులు చేయించుకోవచ్చు థాంక్యూ సర్ థాంక్యూ మేడం చెప్పండి మీరు ఆల్రెడీ ఉదయం వచ్చారు కదా మీరు మార్నింగ్ కోడ్ నెంబర్ చెప్పండి ఈ నెంబరు ఉన్న ఫైల్ తేడా చూపిస్తుంది ఏంటి తేడా ఏంటి ఒకసారి రిపోర్ట్ చెక్ చేయండి నా కోడ్ నెంబర్లు చేస్తారు మా రిపోర్ట్స్ ఎప్పుడు వస్తాయి సిస్టర్ చేస్తారు అమ్మో తొమ్మిది గంటలకి డిన్నర్ చేశావు కదా మళ్ళీ టిఫిన్ తిన్నావా ఏంటి ఏం తినకుండా వెళ్తే టెస్ట్ లో ఏ సమయానికి లంచ్ టైం అయిపోతుంది కదా మిస్ అవుతాం కదా అని బాడీ కాదు మేడం మా రిపోర్ట్స్ మీ నెంబర్ చెప్పండి 3322 ఒక ఐదు నిమిషాలు కూర్చోండి థాంక్యూ రిపోర్ట్స్ తీసుకుని రేపు వస్తే కన్సల్టింగ్ డాక్టర్స్ ఉంటారు వాళ్ళం కలిసి ప్రిస్క్రిప్షన్ తీసుకోవచ్చు కదా ఏమైంది 331 32 కోడ్ యూటర్న్ మార్చేయాలి చాలా ప్రాబ్లం వస్తుంది ఇప్పుడు ఏమైందని షుగర్ కంప్లైంట్ ఉన్న అతనికి బిపి అని బిపి కంప్లైంట్ నెంబర్స్ ఇవ్వలేదు కదా రేపు వాళ్ళు వచ్చి డాక్టర్ని కన్సల్ట్ ముందు ఎవరి రిపోర్ట్స్ వరకు మార్చి ఇచ్చాయి సో ఇక నుంచి భారం నీకు బిపి ఏంటమ్మా వినడానికి విడ్డూరంగా ఉంది మన తిన్న పావలా కదలకుండా పడి ఉండే నీకు బీపీ అంటే నాకు నమ్మబుద్ధి కావడం లేదు నీకు bp అంటే తెలుసా నీకే సాధ్యం అయింది రాకుండా పోతుందా అక్కడ రాసింది కాబట్టే వచ్చినట్టుంది కానీ ఈ బీపీలో నాకు ఒరిజినాలిటీ కనిపించట్లేదు సో మీకు షుగర్ కంప్లైంట్ స్వీట్స్ బందు మీరు ఎక్కువగా స్వీట్లు తొందరగా దిగులు ఫేసు తినడానికి ఫ్రీడం ఉన్నప్పుడు పెద్దగా ఇష్టం ఉండేది కాదు ఇప్పుడు నన్ను పూర్తిగా మానేయమని సరికి ఇష్టం బాగా పెరిగిపోయింది అది సహజం అండి ఇలాంటి అప్పుడే గుండె నిబ్బరం చేసుకొని నిక్కచ్చిగా ఉండాలి నువ్వు అలా పూర్తిగా కట్టడి చేస్తే నాకు అర్జెంటుగా స్వీట్స్ తినాలనిపిస్తుంది స్వీట్స్ ఒక కేజీ పావు కేజీ కూడా పెట్టను మీకే మంచిదండి నాకు బిగ్ నెంబర్ కి తమరు సంపూర్ణ ఆరోగ్యవంతులైన నిన్ను అంటారు ఏంటి తమరు bp పేషెంట్ అన్న సంగతి మర్చిపోయారా పెట్టండి చాలా బాగుంటుంది కాస్త నువ్వు కూడా ఒకసారి ట్రై చెయ్ అబ్బబ్బబ్బ అయ్యో నీకు మంచి కాఫీలు టీలు షుగర్ లెస్ తాగలేదు కాఫీలో సాల్ట్ తినే యోగం ఉండాలే కాని ఎందులో ఉన్న వేసుకోవచ్చు సాల్ట్ కొంతమంది గది లేదు నన్ను ఉడికించాలి రుచి అద్భుతంగా ఉన్నట్టుంది కదా కొప్పుల మీద కప్పులు తాగాలనిపిస్తుంది కదా మాకు తెలుసు తమరు షుగర్ లో ఇడ్లీ ని ఉంచుకొని ముంచుకుని నంచుకుని ఆ అబ్బబ్బబ్బ ఈ గులాబ్ జామున్ కి నేను గులాం రా స్వీట్ అంటే ఇలా ఉండాలి అనుకుంటే అబ్బబ్బబ్బ నా వల్ల కాదు కొంతమందికి మాత్రం అదృష్టం ఉండదు ఎంత స్వీట్ తిన్న ఆ తర్వాత హాట్ హాట్ గా బజ్జీలు తింటేనే వస్తుంది మధ్యం ఉప్పు కొంచెం వేస్తే బెస్ట్ ఇక్కడ బజ్జీలు అంటే ఎవరికి ఇష్టం కానీ సాల్ట్ తినే యోగం లేదు పాపం ఏమన్నా స్వీట్ స్వీట్ ఇద్దరూ తీరిగ్గా కూర్చుని తినడానికి ఇబ్బంది పెడుతున్నారు మనిషి ఎవడైనా స్వీట్ ఉండగలడా ఏవండోయ్ మీరు నాకు విషయం చెప్పండి మానవ జన్మ ఎత్తిన వాడు ఉప్పు లేకుండా చప్పిడి కూరలు తినడం ఎంత దౌర్భాగ్యం ఏమిటి సాల్ట్ అండ్ షుగర్ సంగ్రామం వాడు డయాబెటిక్ షుగర్ తినకూడదు టిడిపిలో ఉన్నారు ఒకరు చూసుకొని బాగా చెప్పుకుంటున్నారు మరి నేను ఈ గులాబ్ జామ్ ని ఈ ఉప్పు ఇలా దొర్లించి దానికి ఒక హోల్ పెట్టి అందులో నిమ్మకాయ పిండి సంపూర్ణ ఆరోగ్యంతో వెలసిన నేను హాయిగా తినాలి నెక్స్ట్ ఈ మిర్చి బజ్జి ని ఇలా ఈ జ్యూస్లో ఏం ఇలా ముంచి తింటూ ఉంటే ఉంటుంది నా సామిరంగా నవ్వుతో నా భవిష్యత్తు లేక ఒక్కొక్కళ్ళకి చెప్పుకుంటున్నారు సార్ అమృత రావు గారు వెరీ సారీ సార్ మా కంప్యూటర్ మిస్టేక్ వల్ల ఒక రిపోర్టు ఒకరికి మారిపోయింది ఇప్పటివరకు నువ్వు తిన్నావా వీళ్ళకి షుగరు సాల్ట్ ఎక్కువయ్యి ఆర్గాన్స్ కాదు బ్రెయిన్ కూడా పని చేస్తున్నట్టు లేదు నువ్వు తిన్న స్వీట్ కి కళ్ళజోడు పెట్టక్"
embeddings1 = model.encode([sentence1], convert_to_tensor=True)
embeddings2 = model.encode([sentence2], convert_to_tensor=True)
cosine_similarities = torch.nn.functional.cosine_similarity(embeddings1, embeddings2)

# Print similarity score
print(f"Similarity score: {cosine_similarities.item()}")