from sentence_transformers import SentenceTransformer, util
import torch
sentences = [
    "వైసిపి వర్సెస్ కూటమి ఏపీలో జోరుగా బెట్టింగ్ ముఖ్య నేతల మెజారిటీపై పందాలు తెలంగాణ గీతం తో పాటు సింబల్ పై సర్కార్ మాత్రం నేతలు కళాకారులతో రేవంత్ చర్చలు మార్కులపై టీఆర్ఎస్ నిరసన పోస్టర్స్ పై మాటల యుద్ధం సీఈఓ జారీ చేసింది టిడిపి ముఖ్య నేతలతో చంద్రబాబు చెల్లి కాన్ఫరెన్స్ లతో సమావేశం చంద్రగిరి డిఎస్పి చరిత్ర రాజ్కుమార్తో స్పెషల్ వీధిలో నిర్లక్ష్యం వహించారని వేటు నియోజకవర్గం ivf ఒక అధునాతన సంతానోత్పత్తి చికిత్స అనేక దంపతులకు తల్లిదండ్రులు కావాలని వారి కలను నెరవేర్చుకోవడానికి సహాయపడుతుంది ఈరోజే ఓ ఎస్ ఎస్ పాటిల్ ని సందర్శించండి బెజవాడలో విగ్రహం పెంచిన ధైర్యం కలుషిత నీటికి నలుగురు బలి 100 మంది కాస్తంత మొగల్రాజపురం ప్రత్యేక వైద్య శిబిరాలు ఏర్పాటు అమలాపురంలో కుల వివక్ష పై కదలిక టీవీ9 కథనాలతో స్పందించిన కేంద్ర ఎస్సీ కమిషన్ సమగ్ర నివేదిక ఇవ్వాలని కలెక్టర్ ఆఫీస్ స్కానింగ్ సెంటర్లపై టీవీ9 పెద్దపల్లి లోని అయ్యప్ప టెంపుల్ లో చోరీ హుండీ పగల కొట్టి డబ్బులు ఎత్తుకెళ్లిన దొంగలు సీసీటీవీ లో రికార్డ్ అయిన నేడు konda పవనాలు విస్తరించేందుకు పరిస్థితులు అనుకూలం నాలుగు రోజుల్లో ఏపీ లోకి మార్చు నేటితో ముగియనున్న చివరి విడత లోక్సభ ఎన్నికల ప్రచారం 57 పార్లమెంట్ సెగ్మెంట్ స్కూల్ ఎల్లుండి ఎన్నికల్లో ఒడిశాలో అసెంబ్లీ పోలీస్ ఇండియా కూటమికి మూడు వందలు ఎన్డీఏ కి 200 సీట్లు ఫలితాలపై కేసులు వాళ్ళ సంచలన వ్యాఖ్యలు టీవీ9 లైవ్ షోలో రాసి ఇచ్చిన సీఎం నేటి నుండి కన్యాకుమారిలో మోతీచూర్ భారీ భద్రత ఏర్పాట్లు చేసిన అధికారులు రాక్ మెమోరియల్ దగ్గరకి కేంద్ర హోం మంత్రి రాక సాయంత్రం తమిళనాడు నుంచి రేణిగుంటకు అమిత్ షా రాత్రికి తిరుమలలో బస్సు రేపు ఉదయం దర్శనం తిరుచి లో తమిళ్ రైతు సంఘాల ఆందోళన కావేరి జలాలను విడుదల చేయాలని కర్ణాటక సర్కార్ కు వ్యతిరేకంగా రైతుల నినాదాలు",
    "సార్ వాడు ఈ అల్పాహారం టేస్ట్ చేయండి కదా చెప్పండి ఇంతవరకు సరోవరం నాకు తెలుగు మాటలు నేర్పించలేదు మీరు కొంచెం టెస్ట్ చేయండి ఎక్స్పీరియన్స్ లేకపోయినా ఎక్స్పరిమెంట్స్ కి తక్కువ లేదు మళ్లీ మీకు వినిపిస్తోంది కొంచెం ఎక్కువ అయినదా చాలా కరెక్ట్గా చేస్తున్నావ్ ఎలా బాగా చేస్తుంటారు వాడు ఇంకొంచెం బూందీ తయారు చేసి ఇందులో కలుపుతారు ఎలా తయారయ్యావ్ లేదురా వాడు పిచ్చి ప్రయోగం చేస్తున్నాడు అని చిన్న కోపం వచ్చింది అంతే గుడ్ మార్నింగ్ సార్ గుడ్ మార్నింగ్ ఎవరు కావాలి సార్ నేను డాక్టర్స్ డయాగ్నస్టిక్ సెంటర్ మీతో మాట్లాడుతాను మీరు ఎప్పుడైనా టోటల్ బాడీ హెల్త్ చెకప్ చేయించుకున్నారా సార్ మీకు చేయించుకునే ఉద్దేశం ఉంటే మా హాస్పిటల్ కి రండి ఖర్చులు 50% డిస్కౌంట్ మీరు 2000 కట్టి హెల్త్ కార్డు తీసుకుంటే మీకు మూడు నెలల పాటు టెస్టులు అదే పొరపాటు మనం పైకి ఎంత ఆరోగ్యంగా కనిపించినా లోపల మనకు తెలియని ఎన్నో ఉన్నాయి ఈ రోజుల్లో వయసుతో సంబంధం లేకుండా బిపి షుగర్ హాట్ కంప్లైంట్స్ లాంటి వస్తున్నాయి సార్ ముందు జాగ్రత్తగా ఇలాంటి టెస్ట్ లన్ని చేయించుకుంటే అన్ని కంట్రోల్ ఉంచుకోవచ్చు మనం ఎలాగూ హెల్త్ చెకప్ లాంటివి చేయించుకోవాలి ఇలాంటి స్కీములు 50% డిస్కౌంట్ ఉన్నప్పుడు మాత్రమే చేయించుకోవాలి ఏ సింటమ్స్ లేనప్పుడు మనకు అనవసరంగా ఈ ఖర్చు ఎందుకు అంటున్న సింటమ్స్ తెలిస్తే అప్పుడు బాబు నీకు అర్థం కావట్లా ఇప్పుడు నువ్వు లావుగా కనిపిస్తున్నావు అదంతా ఆరోగ్యం అందం బలం బొద్దుగా ముద్దుగా కనిపిస్తున్నారు నీ ఫీలింగ్ అదంతా కొలవలేని కొలెస్ట్రా అంటే కొవ్వా అదే ఎక్కువైతే హార్ట్ ప్రాబ్లమ్స్ వస్తాయి మీకు ఉపయోగకరంగా ఉంటుంది ఆలోచించండి సార్ మనసులో ఒక గిన్నె వచ్చి చేరాక అది క్లారిఫై చేసుకునేదాకా కుదురుగా ఉండడం సరే ఆ స్కీమ్ లో మేము జాయిన్ అవుతాను అప్లికేషన్ ఫిల్ చేయనా ఒరేయ్ అరవం లంచ్ పెట్టరా సార్ ఇక్కడ సైన్ చేయండి అది సమయానికి వచ్చారు సార్ మీరు స్క్రీన్ లో చేరండి స్కీమ్లో హెల్త్ చెకప్ కి 50% డిస్కౌంట్ స్కీమ్ పెట్టారు 2000 కి మూడు నెలల పాటు అన్ని టెస్టులు ఫ్రీగా ఇది మీ హెల్త్ కార్డు ఇది మీ కార్డు తీసుకురావాలని కంపల్సరిగా తీసుకొస్తే మంచిది సార్ ఒకవేళ మర్చిపోయిన ఇది మీ కోడ్ నెంబర్ 331 332 ఈ కోడ్ నెంబర్ చెప్పు మీరు అన్ని టెస్టులు చేయించుకోవచ్చు థాంక్యూ సర్ థాంక్యూ మేడం చెప్పండి మీరు ఆల్రెడీ ఉదయం వచ్చారు కదా మీరు మార్నింగ్ కోడ్ నెంబర్ చెప్పండి ఈ నెంబరు ఉన్న ఫైల్ తేడా చూపిస్తుంది ఏంటి తేడా ఏంటి ఒకసారి రిపోర్ట్ చెక్ చేయండి నా కోడ్ నెంబర్లు చేస్తారు మా రిపోర్ట్స్ ఎప్పుడు వస్తాయి సిస్టర్ చేస్తారు అమ్మో తొమ్మిది గంటలకి డిన్నర్ చేశావు కదా మళ్ళీ టిఫిన్ తిన్నావా ఏంటి ఏం తినకుండా వెళ్తే టెస్ట్ లో ఏ సమయానికి లంచ్ టైం అయిపోతుంది కదా మిస్ అవుతాం కదా అని బాడీ కాదు మేడం మా రిపోర్ట్స్ మీ నెంబర్ చెప్పండి 3322 ఒక ఐదు నిమిషాలు కూర్చోండి థాంక్యూ రిపోర్ట్స్ తీసుకుని రేపు వస్తే కన్సల్టింగ్ డాక్టర్స్ ఉంటారు వాళ్ళం కలిసి ప్రిస్క్రిప్షన్ తీసుకోవచ్చు కదా ఏమైంది 331 32 కోడ్ యూటర్న్ మార్చేయాలి చాలా ప్రాబ్లం వస్తుంది ఇప్పుడు ఏమైందని షుగర్ కంప్లైంట్ ఉన్న అతనికి బిపి అని బిపి కంప్లైంట్ నెంబర్స్ ఇవ్వలేదు కదా రేపు వాళ్ళు వచ్చి డాక్టర్ని కన్సల్ట్ ముందు ఎవరి రిపోర్ట్స్ వరకు మార్చి ఇచ్చాయి సో ఇక నుంచి భారం నీకు బిపి ఏంటమ్మా వినడానికి విడ్డూరంగా ఉంది మన తిన్న పావలా కదలకుండా పడి ఉండే నీకు బీపీ అంటే నాకు నమ్మబుద్ధి కావడం లేదు నీకు bp అంటే తెలుసా నీకే సాధ్యం అయింది రాకుండా పోతుందా అక్కడ రాసింది కాబట్టే వచ్చినట్టుంది కానీ ఈ బీపీలో నాకు ఒరిజినాలిటీ కనిపించట్లేదు సో మీకు షుగర్ కంప్లైంట్ స్వీట్స్ బందు మీరు ఎక్కువగా స్వీట్లు తొందరగా దిగులు ఫేసు తినడానికి ఫ్రీడం ఉన్నప్పుడు పెద్దగా ఇష్టం ఉండేది కాదు ఇప్పుడు నన్ను పూర్తిగా మానేయమని సరికి ఇష్టం బాగా పెరిగిపోయింది అది సహజం అండి ఇలాంటి అప్పుడే గుండె నిబ్బరం చేసుకొని నిక్కచ్చిగా ఉండాలి నువ్వు అలా పూర్తిగా కట్టడి చేస్తే నాకు అర్జెంటుగా స్వీట్స్ తినాలనిపిస్తుంది స్వీట్స్ ఒక కేజీ పావు కేజీ కూడా పెట్టను మీకే మంచిదండి నాకు బిగ్ నెంబర్ కి తమరు సంపూర్ణ ఆరోగ్యవంతులైన నిన్ను అంటారు ఏంటి తమరు bp పేషెంట్ అన్న సంగతి మర్చిపోయారా పెట్టండి చాలా బాగుంటుంది కాస్త నువ్వు కూడా ఒకసారి ట్రై చెయ్ అబ్బబ్బబ్బ అయ్యో నీకు మంచి కాఫీలు టీలు షుగర్ లెస్ తాగలేదు కాఫీలో సాల్ట్ తినే యోగం ఉండాలే కాని ఎందులో ఉన్న వేసుకోవచ్చు సాల్ట్ కొంతమంది గది లేదు నన్ను ఉడికించాలి రుచి అద్భుతంగా ఉన్నట్టుంది కదా కొప్పుల మీద కప్పులు తాగాలనిపిస్తుంది కదా మాకు తెలుసు తమరు షుగర్ లో ఇడ్లీ ని ఉంచుకొని ముంచుకుని నంచుకుని ఆ అబ్బబ్బబ్బ ఈ గులాబ్ జామున్ కి నేను గులాం రా స్వీట్ అంటే ఇలా ఉండాలి అనుకుంటే అబ్బబ్బబ్బ నా వల్ల కాదు కొంతమందికి మాత్రం అదృష్టం ఉండదు ఎంత స్వీట్ తిన్న ఆ తర్వాత హాట్ హాట్ గా బజ్జీలు తింటేనే వస్తుంది మధ్యం ఉప్పు కొంచెం వేస్తే బెస్ట్ ఇక్కడ బజ్జీలు అంటే ఎవరికి ఇష్టం కానీ సాల్ట్ తినే యోగం లేదు పాపం ఏమన్నా స్వీట్ స్వీట్ ఇద్దరూ తీరిగ్గా కూర్చుని తినడానికి ఇబ్బంది పెడుతున్నారు మనిషి ఎవడైనా స్వీట్ ఉండగలడా ఏవండోయ్ మీరు నాకు విషయం చెప్పండి మానవ జన్మ ఎత్తిన వాడు ఉప్పు లేకుండా చప్పిడి కూరలు తినడం ఎంత దౌర్భాగ్యం ఏమిటి సాల్ట్ అండ్ షుగర్ సంగ్రామం వాడు డయాబెటిక్ షుగర్ తినకూడదు టిడిపిలో ఉన్నారు ఒకరు చూసుకొని బాగా చెప్పుకుంటున్నారు మరి నేను ఈ గులాబ్ జామ్ ని ఈ ఉప్పు ఇలా దొర్లించి దానికి ఒక హోల్ పెట్టి అందులో నిమ్మకాయ పిండి సంపూర్ణ ఆరోగ్యంతో వెలసిన నేను హాయిగా తినాలి నెక్స్ట్ ఈ మిర్చి బజ్జి ని ఇలా ఈ జ్యూస్లో ఏం ఇలా ముంచి తింటూ ఉంటే ఉంటుంది నా సామిరంగా నవ్వుతో నా భవిష్యత్తు లేక ఒక్కొక్కళ్ళకి చెప్పుకుంటున్నారు సార్ అమృత రావు గారు వెరీ సారీ సార్ మా కంప్యూటర్ మిస్టేక్ వల్ల ఒక రిపోర్టు ఒకరికి మారిపోయింది ఇప్పటివరకు నువ్వు తిన్నావా వీళ్ళకి షుగరు సాల్ట్ ఎక్కువయ్యి ఆర్గాన్స్ కాదు బ్రెయిన్ కూడా పని చేస్తున్నట్టు లేదు నువ్వు తిన్న స్వీట్ కి కళ్ళజోడు పెట్టక్"
]

model = SentenceTransformer("l3cube-pune/telugu-sentence-bert-nli")

embedding_1= model.encode(sentences[0], convert_to_tensor=True)
embedding_2 = model.encode(sentences[1], convert_to_tensor=True)

cosine_similarities = torch.nn.functional.cosine_similarity(embedding_1, embedding_2)

print(f"Similarity score: {cosine_similarities.item()}")