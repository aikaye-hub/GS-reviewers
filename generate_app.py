import json

CARDS = [
{"id": 16, "cat": "Appendicitis", "q": "An Alvarado score of 8 would suggest:", "source": "Alvarado 1986", "correct": "High probability of appendicitis — surgical exploration indicated", "choices": ["High probability of appendicitis — surgical exploration indicated", "Low probability — safe for discharge with outpatient follow-up", "Intermediate probability — CT scan recommended", "Indeterminate — requires laparoscopic diagnostic exploration only"], "explanation": "Alvarado scoring: ≥7 = high probability → appendectomy; 5-6 = intermediate → CT/observation; <5 = low probability. MANTRELS: Migration(1), Anorexia(1), Nausea/Vomiting(1), Tenderness RLQ(2), Rebound(1), Elevated temp(1), Leukocytosis(2), Shift(1). Max = 10."},
{"id": 17, "cat": "Appendicitis", "q": "Pain in the RLQ elicited by passive extension of the right hip — with the patient lying on their left side — is called:", "source": "PSGS Review 2026", "correct": "Psoas sign (suggests retrocecal appendix)", "choices": ["Psoas sign (suggests retrocecal appendix)", "Obturator sign (suggests pelvic appendix)", "Rovsing sign (suggests peritoneal irritation)", "Blumberg sign (rebound tenderness)"], "explanation": "Psoas sign = RLQ pain with right hip extension (psoas muscle irritation) → retrocecal appendix. Obturator sign = RLQ pain with right hip internal rotation → pelvic appendix. Rovsing sign = RLQ pain when palpating the LLQ → shared peritoneal irritation."},
{"id": 18, "cat": "Appendicitis", "q": "What is the preferred initial imaging for suspected appendicitis in a pregnant patient?", "source": "ACOG / SAGES", "correct": "Ultrasound, followed by MRI if inconclusive", "choices": ["Ultrasound, followed by MRI if inconclusive", "CT abdomen/pelvis with contrast", "MRI with gadolinium", "X-ray abdomen (scout film)"], "explanation": "In pregnancy: start with U/S (no radiation, safe, widely available). If inconclusive, MRI (no gadolinium, no radiation) is next. CT is reserved for when MRI is unavailable and diagnosis is uncertain — not first-line due to fetal radiation. Non-contrast CT is acceptable if needed."},
{"id": 19, "cat": "Appendicitis", "q": "The APPAC trial demonstrated that antibiotics alone for uncomplicated appendicitis had what success rate at 1 year?", "source": "APPAC Trial (Salminen, JAMA 2015)", "correct": "73% (27% eventually required appendectomy within 1 year)", "choices": ["73% (27% eventually required appendectomy within 1 year)", "95% (only 5% failure, same as surgery recurrence)", "50% (comparable to a coin flip, surgery preferred)", "88% (failure mostly in elderly patients)"], "explanation": "APPAC trial: IV ertapenem × 3 days → oral levofloxacin + metronidazole × 7 days. 73% success at 1 year. At 5-year follow-up ~40% eventually needed appendectomy. No increased complication rate vs surgery. Antibiotics are a viable option for uncomplicated appendicitis if patient prefers non-surgical management."},
{"id": 20, "cat": "Appendicitis", "q": "A CT scan shows a 4cm periappendiceal abscess. The most appropriate initial management is:", "source": "PSGS Review 2026", "correct": "Percutaneous drainage + IV antibiotics → interval appendectomy 6-8 weeks later", "choices": ["Percutaneous drainage + IV antibiotics → interval appendectomy 6-12 weeks later", "Immediate emergency appendectomy", "IV antibiotics alone without drainage", "Laparoscopic appendectomy with intraoperative drainage"], "explanation": "For well-contained abscess ≥3cm: percutaneous drainage + antibiotics first to control sepsis, then interval (elective) appendectomy 6-12 weeks later when inflammation has resolved. Abscess <3cm: antibiotics alone may suffice. Diffuse peritonitis or failed drainage → immediate surgery."},
{"id": 21, "cat": "Appendicitis", "q": "Laparoscopic appendectomy in pregnancy is considered:", "source": "SAGES Guidelines", "correct": "Safe in all three trimesters", "choices": ["Safe in all three trimesters", "Safe only in the first trimester", "Safe only in the second trimester; open preferred in 3rd trimester", "Contraindicated — open appendectomy required in all pregnant patients"], "explanation": "Laparoscopic appendectomy is safe in ALL trimesters of pregnancy. In the 3rd trimester, trocar placement may need modification due to uterine size (open may sometimes be preferred). Uncontrolled appendicitis carries a fetal loss rate of 3-5% from perforation — surgical delay is more dangerous than the operation."},
{"id": 22, "cat": "Appendicitis", "q": "Compared to adults, children with appendicitis have a higher perforation rate (30-50%) primarily because:", "source": "PSGS Review 2026", "correct": "The omentum is underdeveloped, limiting walling-off of perforation", "choices": ["The omentum is underdeveloped, limiting walling-off of perforation", "Children have a longer appendix, delaying obstruction", "Inflammatory response is blunted in children", "Children receive antibiotics more frequently, masking symptoms"], "explanation": "Children have: (1) underdeveloped omentum → can't wall off perforation, (2) thinner appendix wall → faster transmural necrosis, (3) less reliable symptoms → delayed presentation, (4) atypical exam → delayed diagnosis. All lead to higher perforation rates."},
{"id": 23, "cat": "Appendicitis", "q": "A 2.5 cm appendiceal carcinoid tumor with no lymph node involvement is found during appendectomy. Next step:", "source": "NCCN / PSGS Review 2026", "correct": "Right hemicolectomy", "choices": ["Right hemicolectomy", "Appendectomy alone — margins are sufficient", "Adjuvant chemotherapy without further surgery", "Observation — carcinoids rarely metastasize"], "explanation": "Appendiceal carcinoid management by size: <1cm → appendectomy alone (99% cure). 1-2cm → appendectomy alone if margins clear and no adverse features. >2cm → right hemicolectomy (higher metastatic potential). Also: hemicolectomy for any carcinoid with lymph node involvement or base involvement."},
{"id": 24, "cat": "Appendicitis", "q": "During appendectomy for a mucocele, the most important technical consideration is:", "source": "PSGS Review 2026", "correct": "Handle gently — rupture causes pseudomyxoma peritonei", "choices": ["Handle gently — rupture causes pseudomyxoma peritonei", "Always perform right hemicolectomy regardless of size", "Send frozen section immediately — surgery must stop if malignant", "Irrigate with povidone-iodine to sterilize mucin if leakage occurs"], "explanation": "Mucocele (from LAMN — low-grade appendiceal mucinous neoplasm) must be handled without rupture. If it ruptures, mucin seeds the peritoneum → pseudomyxoma peritonei ('jelly belly'). Treatment of pseudomyxoma: cytoreductive surgery (CRS) + HIPEC. Careful extraction (may need Pfannenstiel incision or specimen bag)."},
{"id": 25, "cat": "Appendicitis", "q": "Elderly patients with appendicitis have 4-8× higher mortality than younger adults primarily due to:", "source": "PSGS Review 2026", "correct": "Atypical presentation leading to delayed diagnosis and higher perforation rate at presentation", "choices": ["Atypical presentation leading to delayed diagnosis and higher perforation rate at presentation", "Elderly patients have a longer, more tortuous appendix prone to obstruction", "Age-related immune deficiency causes more virulent bacterial infections", "Higher rates of malignancy masquerading as appendicitis"], "explanation": "In the elderly: blunted fever response, less guarding/rigidity, vague pain → delayed diagnosis. >50% present with perforation. Combined with medical comorbidities, the mortality rises dramatically. Maintain a high index of suspicion — classic MANTRELS features are often absent."},
{"id": 189, "cat": "Appendicitis", "q": "A 3 cm appendiceal carcinoid (NET) is found at appendectomy. What additional procedure is required?", "source": "NCCN Appendiceal NET Guidelines", "correct": "Right hemicolectomy (carcinoid >2 cm has significant risk of nodal metastasis)", "choices": ["Right hemicolectomy (carcinoid >2 cm has significant risk of nodal metastasis)", "Simple appendectomy is sufficient for all carcinoids", "Chemotherapy only", "Observation with octreotide scan"], "explanation": "Appendiceal NETs (carcinoids): <1 cm — simple appendectomy (curative, <2% metastasis); 1–2 cm — appendectomy (most cases), consider right hemicolectomy if positive margins, mesoappendix invasion, or high-grade features; >2 cm — right hemicolectomy (metastasis risk 30%). Key threshold: >2 cm = right hemicolectomy. Lymph node metastases → Dukes staging; systemic spread rare for appendiceal NETs."},
{"id": 190, "cat": "Appendicitis", "q": "A 28-year-old pregnant woman (22 weeks) presents with right-sided pain that has migrated superiorly. CT confirms acute appendicitis. What is the management?", "source": "Appendicitis in Pregnancy / SAGES", "correct": "Laparoscopic appendectomy (safe throughout pregnancy; fetal loss rate higher with perforated vs non-perforated)", "choices": ["Laparoscopic appendectomy (safe throughout pregnancy; fetal loss rate higher with perforated vs non-perforated)", "Delay surgery until after delivery", "IV antibiotics only — surgery contraindicated in pregnancy", "Open appendectomy mandatory in pregnancy"], "explanation": "Appendicitis in pregnancy: surgical treatment is indicated. Laparoscopic appendectomy is safe in all trimesters (port placement adjusted for uterine size). Delay risks perforation (fetal loss 20–35% with perforation vs ~3% without). Antibiotic-only management has high recurrence rates. The appendix migrates superiorly and laterally as pregnancy progresses (significant by 2nd trimester), which may delay diagnosis."},
{"id": 191, "cat": "Appendicitis", "q": "A patient is treated non-operatively for a periappendiceal abscess (appendicitis with abscess/phlegmon). What is the recommended timing of interval appendectomy?", "source": "EAST / Interval Appendectomy Guidelines", "correct": "6–8 weeks after resolution (debated; some advocate skip interval appendectomy in uncomplicated cases)", "choices": ["6–8 weeks after resolution (debated; some advocate skip interval appendectomy in uncomplicated cases)", "Immediate surgery during the acute episode", "12 months after resolution", "Never — interval appendectomy not recommended"], "explanation": "Non-operative management of appendiceal abscess/phlegmon: drain + antibiotics. Interval appendectomy traditionally performed 6–8 weeks later. Modern evidence: ~80% never have recurrence; some guidelines now suggest colonoscopy to exclude malignancy (especially >40 years), and skip appendectomy unless recurrence or malignancy concern. Colonoscopy is essential in older patients to rule out cecal cancer presenting as appendicitis."},
{"id": 192, "cat": "Appendicitis", "q": "Pseudomyxoma peritonei (PMP) is most commonly caused by a ruptured appendiceal mucinous neoplasm. What is the current recommended treatment for resectable PMP?", "source": "PMP / Peritoneal Malignancy", "correct": "Cytoreductive surgery (CRS) + hyperthermic intraperitoneal chemotherapy (HIPEC)", "choices": ["Cytoreductive surgery (CRS) + hyperthermic intraperitoneal chemotherapy (HIPEC)", "Systemic chemotherapy only", "Appendectomy alone", "Palliative surgery only"], "explanation": "PMP: diffuse peritoneal mucin deposits from appendiceal mucinous neoplasm (LAMN or mucinous adenocarcinoma). Optimal treatment: cytoreductive surgery (peritonectomy, removal of all visible disease) + HIPEC (heated intraperitoneal chemotherapy, usually mitomycin-C). CRS-HIPEC achieves 5-year survival >80% for low-grade PMP (LAMN origin) in specialized centers. Systemic chemo has poor peritoneal penetration."},
{"id": 193, "cat": "Appendicitis", "q": "The Alvarado score is used to stratify the probability of acute appendicitis. Which finding carries a score of 2 (the highest weight in the original scale)?", "source": "Alvarado Score / Appendicitis Diagnosis", "correct": "Leukocytosis (WBC >10,000) — scores 2 points", "choices": ["Leukocytosis (WBC >10,000) — scores 2 points", "Rebound tenderness — scores 2 points", "RLQ tenderness — scores 2 points", "Migration of pain to RLQ — scores 2 points"], "explanation": "Alvarado score MANTRELS: Migration of pain to RLQ (1), Anorexia (1), Nausea/vomiting (1), Tenderness in RLQ (2), Rebound tenderness (1), Elevated temperature (1), Leukocytosis (2), Shift to left (1). Total 10 points. Score ≤4: unlikely appendicitis; 5–6: possible; 7–8: probable (operate or CT); 9–10: almost certain (operate). Leukocytosis and RLQ tenderness each score 2."},
{"id": 57, "cat": "BDI", "q": "In the Strasberg-Bismuth classification, a Type E2 injury describes:", "source": "Strasberg Classification / SAGES", "correct": "Transection of the common hepatic duct <2 cm from the hepatic confluence", "choices": ["Transection of the common hepatic duct <2 cm from the hepatic confluence", "Transection of the CHD ≥2 cm from the hepatic confluence", "Complete occlusion of the right sectoral duct without transection", "Lateral injury to the common hepatic duct without complete transection"], "explanation": "Strasberg E injuries (CHD/CBD transections): E1 = ≥2cm below confluence; E2 = <2cm below confluence; E3 = at confluence; E4 = separation of right and left hepatic ducts; E5 = E1-E4 + right hepatic duct injury. All E injuries require Roux-en-Y hepaticojejunostomy. The closer to the confluence, the more complex the repair."},
{"id": 58, "cat": "BDI", "q": "The Critical View of Safety (CVS) during laparoscopic cholecystectomy requires ALL THREE criteria — which answer correctly lists them?", "source": "SAGES Safe Cholecystectomy Program", "correct": "(1) Hepatocystic triangle cleared of fat/fibrous tissue; (2) lower 1/3 of GB dissected free from liver bed; (3) only 2 structures (cystic duct + cystic artery) entering GB", "choices": ["(1) Hepatocystic triangle cleared of fat/fibrous tissue; (2) lower 1/3 of GB dissected free from liver bed; (3) only 2 structures (cystic duct + cystic artery) entering GB", "(1) Only two structures entering the GB; (2) cystic artery clipped before cystic duct", "(1) Intraoperative cholangiogram performed; (2) CBD visualized and spared; (3) cystic duct clipped × 2", "(1) GB fully detached from liver bed; (2) common bile duct identified; (3) no bile leakage observed"], "explanation": "CVS = ALL THREE criteria MUST be met before clipping: (1) Hepatocystic triangle fully cleared of fat and fibrous tissue; (2) Lower 1/3 of gallbladder dissected free from the cystic plate/liver bed; (3) Only TWO structures (cystic duct + cystic artery) seen entering the gallbladder. If CVS not achievable → IOC → call for help → subtotal cholecystectomy → convert to open. NEVER clip blindly."},
{"id": 59, "cat": "BDI", "q": "A Strasberg Type A bile duct injury (cystic duct leak) recognized postoperatively is best managed by:", "source": "SAGES / ASGE Guidelines", "correct": "ERCP with biliary stent placement", "choices": ["ERCP with biliary stent placement", "Immediate return to OR for Roux-en-Y hepaticojejunostomy", "Percutaneous transhepatic cholangiography (PTC) drainage alone", "Conservative management with observation and IV antibiotics only"], "explanation": "Type A = cystic duct stump leak or small duct of Luschka — the CBD is intact. Preferred: ERCP + biliary stent (reduces sphincter resistance, allows cystic duct stump to heal). Percutaneous drain may be needed for biloma. Roux-en-Y hepaticojejunostomy is overkill for Type A and reserved for Types B-E (complete duct injuries)."},
{"id": 60, "cat": "BDI", "q": "When a BDI is recognized postoperatively in a patient with bile peritonitis and sepsis, the MOST IMPORTANT first principle is:", "source": "SAGES / PSGS Review 2026", "correct": "Control sepsis first (drain, antibiotics, resuscitate) — definitive repair in 6-8 weeks", "choices": ["Control sepsis first (drain, antibiotics, resuscitate) — definitive repair in 6-8 weeks", "Immediate operative repair at the same admission", "ERCP stenting as first-line management", "Percutaneous drainage only; repair is not needed"], "explanation": "BDI recognized postoperatively with bile peritonitis: (1) Control sepsis first — drain the bile collection, IV antibiotics, resuscitate. (2) Define anatomy with MRCP or ERCP/PTC (do NOT attempt repair until anatomy is clarified). (3) Definitive repair (Roux-en-Y hepaticojejunostomy) is deferred 6–8 weeks after acute inflammation and sepsis have resolved. If concurrent RHA injury → higher risk of ischemic stricture and repair failure. Early referral to a hepatobiliary surgeon is mandatory."},
{"id": 61, "cat": "BDI", "q": "The most common mechanism of bile duct injury during laparoscopic cholecystectomy (Stewart-Way Class I) involves:", "source": "SAGES Safe Cholecystectomy Program", "correct": "Misidentifying the common bile duct as the cystic duct due to inadequate dissection", "choices": ["Misidentifying the common bile duct as the cystic duct due to inadequate dissection", "Excessive bleeding leading to blind clipping of the CBD", "Thermal injury from electrocautery during dissection", "Excessive traction on the gallbladder causing CBD avulsion"], "explanation": "Stewart-Way Class I (most common): CBD is mistaken for the cystic duct due to inadequate hepatocystic triangle dissection. The CBD is clipped and divided — often the 'classic' laparoscopic BDI. Class II: excessive bleeding + blind clipping. Class III: misidentified right hepatic duct. Class IV: right hepatic artery + right hepatic duct injury. Prevention = achieving the Critical View of Safety."},
{"id": 62, "cat": "BDI", "q": "Concurrent right hepatic artery (RHA) injury with a major BDI is significant because:", "source": "SAGES / PSGS Review 2026", "correct": "It devascularizes the bile duct, leading to ischemic stricture and higher failure of repair", "choices": ["It devascularizes the bile duct, leading to ischemic stricture and higher failure of repair", "It increases infection risk but does not affect repair outcomes", "RHA injury requires hepatectomy which takes precedence over bile duct repair", "It is a marker of more extensive dissection, not independently prognostic"], "explanation": "RHA injury occurs in ~12% of major BDIs. Consequences: bile duct loses its arterial supply → ischemic bile duct → stricture even after technically correct hepaticojejunostomy. May also cause liver infarction/abscess. This is the single worst prognostic factor. Diagnosis: Doppler US or CT angiogram. Management: refer to hepatobiliary center — may need vascular reconstruction."},
{"id": 171, "cat": "BDI", "q": "The Strasberg classification of bile duct injuries extends the Bismuth system to include cystic duct leaks and minor ductal injuries. Which Strasberg type represents the classic 'major BDI' — complete transection of the common hepatic duct?", "source": "Strasberg / BDI Classification", "correct": "Type E (equivalent to Bismuth I–V: injuries to the main bile duct)", "choices": ["Type E (equivalent to Bismuth I–V: injuries to the main bile duct)", "Type A (cystic duct leak)", "Type C (right sectoral duct leak)", "Type D (lateral injury to main duct)"], "explanation": "Strasberg classification: A = cystic duct leak/cystic artery bleed; B = occluded right sectoral duct; C = transected right sectoral duct (biloma); D = lateral injury to main duct; E1–E5 = injuries to hepatic duct at increasing levels (E1 = >2cm from confluence, E5 = right hepatic duct + confluence). Types A-D occur at LC; Type E injuries are the most severe and require reconstructive surgery."},
{"id": 172, "cat": "BDI", "q": "Bismuth classification describes BDI based on the level of injury relative to the hepatic duct confluence. Bismuth V is the most complex. What does it represent?", "source": "Bismuth BDI Classification", "correct": "Involvement of the right sectoral duct with aberrant drainage and confluence injury", "choices": ["Involvement of the right sectoral duct with aberrant drainage and confluence injury", "Complete transection >2 cm from confluence", "Injury at the confluence", "Stricture of the CHD <2 cm from confluence"], "explanation": "Bismuth levels: I = CHD stump >2cm; II = CHD stump <2cm; III = at the confluence (hepatic duct junction intact); IV = confluence destruction (right and left separated); V = involvement of aberrant right sectoral hepatic duct (entering CHD separately). Higher Bismuth = worse prognosis, more complex reconstruction, may require partial hepatectomy."},
{"id": 173, "cat": "BDI", "q": "A BDI is discovered 3 days after laparoscopic cholecystectomy when the patient develops jaundice. CT shows a biloma. What is the IMMEDIATE priority of management?", "source": "BDI Management / SAGES", "correct": "Biliary decompression via ERCP with stenting + percutaneous drainage of biloma", "choices": ["Biliary decompression via ERCP with stenting + percutaneous drainage of biloma", "Immediate surgical bile duct repair", "Observation and antibiotics only", "Refer to transplant center immediately"], "explanation": "Immediate management of BDI: (1) Control sepsis — drain biloma/biliary collections percutaneously; (2) Define injury — MRCP/ERCP to characterize anatomy; (3) ERCP stenting for minor injuries (Strasberg A-D, partial transections). Definitive surgical repair (hepaticojejunostomy) should be delayed until: patient is stable, inflammation resolved (4–6 weeks minimum), and preferably performed at a hepatobiliary center. Early rushed repair → worse outcomes."},
{"id": 174, "cat": "BDI", "q": "During laparoscopic cholecystectomy, the classic 'misidentification' mechanism of BDI occurs when the surgeon mistakes the common bile duct for the cystic duct. This most often occurs due to:", "source": "BDI Prevention / Critical View of Safety", "correct": "Failure to achieve the Critical View of Safety (CVS) — inadequate dissection of Calot's triangle", "choices": ["Failure to achieve the Critical View of Safety (CVS) — inadequate dissection of Calot's triangle", "Excessive traction on the gallbladder fundus", "Aberrant right hepatic artery", "Intraoperative cholangiogram not performed"], "explanation": "The Critical View of Safety (CVS) — mandatory before clipping: (1) Calot's triangle completely dissected free of fat/fibrous tissue; (2) lower third of gallbladder dissected from liver bed; (3) only two structures (cystic duct and cystic artery) seen entering gallbladder. CVS is the most effective strategy to prevent BDI. Intraoperative cholangiography detects but does not prevent BDI; CVS prevents it."},
{"id": 175, "cat": "BDI", "q": "After successful biliary reconstruction with Roux-en-Y hepaticojejunostomy for a Bismuth IV BDI, what is the most important long-term complication to monitor?", "source": "BDI Long-term Outcomes", "correct": "Anastomotic stricture (occurs in ~20–30%; causes recurrent cholangitis and secondary biliary cirrhosis)", "choices": ["Anastomotic stricture (occurs in ~20–30%; causes recurrent cholangitis and secondary biliary cirrhosis)", "Bile duct carcinoma", "Hepatic artery thrombosis", "Choledocholithiasis"], "explanation": "Long-term follow-up after biliary reconstruction: anastomotic stricture occurs in 10–30%, manifesting as recurrent cholangitis, jaundice, pruritus, or progressive liver failure. Annual LFTs and imaging surveillance. Strictures detected early: percutaneous transhepatic dilation or revision hepaticojejunostomy. Untreated anastomotic stricture → secondary biliary cirrhosis, portal hypertension, and liver failure."},
{"id": 176, "cat": "BDI", "q": "During laparoscopic cholecystectomy, intraoperative cholangiography (IOC) is performed due to unclear anatomy. It shows contrast flowing freely into the duodenum, no filling defect, but the cystic duct appears to insert directly into the right hepatic duct. What should the surgeon do?", "source": "BDI Prevention / Cholangiography", "correct": "Recognize aberrant anatomy and modify dissection — do not clip the 'cystic duct' until anatomy is certain", "choices": ["Recognize aberrant anatomy and modify dissection — do not clip the 'cystic duct' until anatomy is certain", "Clip and divide as usual — the right hepatic duct can be safely divided", "Convert to open immediately without further evaluation", "Abort and close; plan ERCP"], "explanation": "Aberrant bile duct anatomy (cystic duct inserting into right hepatic duct, low CHD insertion, etc.) is a major risk factor for BDI. IOC demonstrating aberrant anatomy: the surgeon must reassess, may need further dissection or open conversion. The RIGHT HEPATIC DUCT must NEVER be clipped. This is precisely the scenario that IOC is designed to identify and prevent from causing BDI."},
{"id": 177, "cat": "BDI", "q": "Mirizzi syndrome results from an impacted gallstone in the cystic duct or infundibulum causing extrinsic compression of the common hepatic duct. Csendes Type II Mirizzi involves what additional finding?", "source": "Mirizzi Syndrome / Biliary Surgery", "correct": "Cholecystocholedochal fistula (stone has eroded into the CHD, up to one-third of its circumference)", "choices": ["Cholecystocholedochal fistula (stone has eroded into the CHD, up to one-third of its circumference)", "Extrinsic compression only without fistula", ">2/3 fistula involvement of CHD", "Complete destruction of CHD"], "explanation": "Csendes classification: Type I = extrinsic compression only; Type II = fistula involving <1/3 CHD circumference; Type III = fistula 1/3–2/3 CHD; Type IV = fistula >2/3 CHD or complete destruction. Surgical management escalates with type: Type I → cholecystectomy; Type II → partial cholecystectomy + primary closure/biliary reconstruction; Types III–IV → biliary-enteric reconstruction (hepaticojejunostomy)."},
{"id": 178, "cat": "BDI", "q": "A choledochal cyst is classified by the Todani system. Type I (most common, ~75%) involves which structure?", "source": "Choledochal Cyst / Todani Classification", "correct": "Fusiform dilation of the entire extrahepatic common bile duct", "choices": ["Fusiform dilation of the entire extrahepatic common bile duct", "Dilation of the intrahepatic ducts only (Caroli's disease)", "Choledochocele (dilation of intramural CBD)", "Diverticulum of extrahepatic duct"], "explanation": "Todani classification: Type I (most common) = fusiform/cystic dilation of extrahepatic CBD; Type II = diverticulum of extrahepatic duct; Type III = choledochocele (intramural CBD/intraduodenal); Type IV = combined intra + extrahepatic dilation (2nd most common); Type V = Caroli disease (intrahepatic only). Management: excision of cyst + biliary reconstruction (hepaticojejunostomy) — due to malignancy risk (~3–15% carcinoma if left unresected)."},
{"id": 179, "cat": "BDI", "q": "Primary sclerosing cholangitis (PSC) is strongly associated with which inflammatory bowel disease, and what is its definitive treatment?", "source": "AASLD PSC Guidelines", "correct": "Ulcerative colitis (~70% of PSC cases); liver transplantation is the only definitive treatment", "choices": ["Ulcerative colitis (~70% of PSC cases); liver transplantation is the only definitive treatment", "Crohn's disease; ursodeoxycholic acid is curative", "Ulcerative colitis; colectomy cures PSC", "Microscopic colitis; cholangiocarcinoma surveillance only"], "explanation": "PSC: fibro-obliterative inflammation of intra- and extrahepatic bile ducts → multifocal strictures, 'beads on a string' on MRCP. ~70% have concomitant UC. No medical therapy (including UDCA) improves survival. Liver transplantation is the only definitive treatment (5-yr survival >80%). Annual CA 19-9, MRCP surveillance for cholangiocarcinoma (lifetime risk 10–15%)."},
{"id": 51, "cat": "Breast/Pregnancy", "q": "What is the first-line imaging modality for a pregnant patient presenting with a breast mass?", "source": "NCCN Breast v1.2026 / Philippine CPG 2025", "correct": "Ultrasound", "choices": ["Ultrasound", "Mammogram with abdominal shielding", "MRI without gadolinium", "PET/CT with fetal shielding"], "explanation": "Ultrasound is first-line in pregnancy — no radiation, safe, widely available, excellent for distinguishing solid vs cystic mass. Mammography is safe in pregnancy (low fetal dose with shielding) but is second-line. MRI without gadolinium is safe and valuable for staging. PET/CT and bone scan should be avoided due to radiation and FDG fetal risk."},
{"id": 52, "cat": "Breast/Pregnancy", "q": "A pregnant patient needs sentinel lymph node biopsy for breast cancer. Which mapping agent is safe to use?", "source": "NCCN Breast v1.2026", "correct": "Technetium-99m (Tc-99m) radioactive colloid", "choices": ["Technetium-99m (Tc-99m) radioactive colloid", "Isosulfan blue (lymphazurin)", "Methylene blue", "ICG (indocyanine green) fluorescence"], "explanation": "Only Tc-99m is approved/safe for SLNB in pregnancy (fetal radiation dose <5 mGy — below the 50 mGy threshold for fetal harm). Blue dyes (isosulfan blue, methylene blue, patent blue) are CONTRAINDICATED — risk of severe anaphylaxis and unknown fetal effects. ICG lacks sufficient pregnancy safety data. Tc-99m SLNB is routinely performed in pregnancy."},
{"id": 53, "cat": "Breast/Pregnancy", "q": "During which gestational period is chemotherapy absolutely contraindicated in a pregnant breast cancer patient?", "source": "NCCN Breast v1.2026 / Philippine CPG 2025", "correct": "First trimester (weeks 1–12, organogenesis)", "choices": ["First trimester (weeks 1–12, organogenesis)", "Second trimester only (rapid fetal growth phase)", "Third trimester only (neonatal exposure risk)", "Chemotherapy is safe at any gestational age"], "explanation": "Chemotherapy is absolutely contraindicated in the 1st trimester (organogenesis) due to high teratogenicity risk. From 14 weeks (2nd trimester) onwards, AC regimen (doxorubicin + cyclophosphamide) is considered relatively safe. Stop chemo ≥3 weeks before delivery to avoid neonatal cytopenias. Target delivery ≥37 weeks."},
{"id": 54, "cat": "Breast/Pregnancy", "q": "Trastuzumab (Herceptin) is contraindicated in pregnancy because:", "source": "NCCN Breast v1.2026", "correct": "It causes oligohydramnios and fetal renal tubular dysplasia", "choices": ["It causes oligohydramnios and fetal renal tubular dysplasia", "It crosses the placenta and directly inhibits fetal cardiac development", "It causes limb reduction defects (similar to thalidomide)", "It is teratogenic only in the first trimester and safe after 14 weeks"], "explanation": "Trastuzumab (anti-HER2): crosses placenta, accumulates in fetal kidney, causes oligohydramnios (reduced amniotic fluid) and fetal renal tubular dysplasia — potentially fatal. Contraindicated throughout pregnancy. Also contraindicated: pertuzumab, tamoxifen (Goldenhar-like syndrome), CDK4/6 inhibitors, bevacizumab, methotrexate. Safe: AC regimen, Tc-99m for SLNB."},
{"id": 55, "cat": "Breast/Pregnancy", "q": "A pregnant patient at 18 weeks is diagnosed with Stage II breast cancer. When should surgery be performed?", "source": "NCCN Breast v1.2026 / Philippine CPG 2025", "correct": "As soon as feasible — surgery is safe at all gestational ages", "choices": ["As soon as feasible — surgery is safe at all gestational ages", "Delay until the third trimester to allow fetal maturation", "Delay until after delivery to minimize anesthetic risk", "Perform cesarean section first then immediately proceed to mastectomy"], "explanation": "Surgery is safe at ALL gestational ages. Surgical delay solely for pregnancy is not recommended — it may worsen prognosis. Anesthetic considerations: avoid hypoxia and hypotension (fetal risk). In 1st trimester: mastectomy preferred (avoid radiation). In 2nd/3rd trimester: BCS + post-delivery radiation is an option. Immediate reconstruction should be deferred until after delivery."},
{"id": 56, "cat": "Breast/Pregnancy", "q": "Breastfeeding after breast cancer treatment is contraindicated during:", "source": "NCCN Breast v1.2026", "correct": "Chemotherapy, trastuzumab, or tamoxifen treatment", "choices": ["Chemotherapy, trastuzumab, or tamoxifen treatment", "Any period following breast-conserving surgery, due to radiation risk", "The first 6 months postpartum regardless of treatment status", "All periods after breast cancer diagnosis — breastfeeding is permanently contraindicated"], "explanation": "Breastfeeding: Contraindicated during chemotherapy (drugs secreted in breast milk), trastuzumab, and tamoxifen. Also reduced milk production from ipsilateral irradiated breast. Breastfeeding from the contralateral breast may be possible if patient is on no systemic therapy. Fertility counseling and reproductive endocrinology referral should be offered early."},
{"id": 180, "cat": "Breast/Pregnancy", "q": "A 52-year-old woman has a 2.5 cm IDC of the right breast (T2 N0 M0). She desires breast conservation. What margins are considered adequate after breast-conserving surgery (BCS)?", "source": "SSO/ASTRO Margins Guideline 2014", "correct": "No ink on tumor (no tumor at inked margin) for invasive cancer", "choices": ["No ink on tumor (no tumor at inked margin) for invasive cancer", "≥2 mm margins", "≥1 cm margins", "Frozen section with ≥5 mm margins"], "explanation": "SSO/ASTRO/ASCO 2014 consensus: for invasive breast cancer treated with BCS + whole-breast radiation, 'no ink on tumor' is the standard. Wider margins do not reduce local recurrence. For DCIS, ≥2 mm margins are recommended. 'No ink on tumor' reduces re-excision rates and is clinically non-inferior to wider margins with adjuvant radiation."},
{"id": 181, "cat": "Breast/Pregnancy", "q": "BRCA1 mutations are associated with which breast cancer subtype most frequently, and how does this influence chemotherapy response?", "source": "BRCA / Breast Cancer Oncology", "correct": "Triple-negative breast cancer (ER−/PR−/HER2−); more sensitive to platinum-based chemotherapy", "choices": ["Triple-negative breast cancer (ER−/PR−/HER2−); more sensitive to platinum-based chemotherapy", "HER2-amplified; responds to trastuzumab", "Luminal A (ER+); resistant to all chemotherapy", "Inflammatory; responds only to bevacizumab"], "explanation": "BRCA1-associated breast cancers are predominantly triple-negative (ER−/PR−/HER2−) and high-grade. Because BRCA1 is a DNA repair gene (homologous recombination), BRCA1-mutated tumors are particularly sensitive to: (1) platinum agents (cisplatin/carboplatin), (2) PARP inhibitors (olaparib, talazoparib). BRCA2-associated tumors are more commonly luminal (ER+) and also PARP-inhibitor sensitive."},
{"id": 182, "cat": "Breast/Pregnancy", "q": "Inflammatory breast cancer (IBC) presents with skin erythema, peau d'orange, warmth, and rapid enlargement. It is classified as at least stage IIIB. What is the correct treatment sequence?", "source": "NCCN Breast Cancer Guidelines", "correct": "Neoadjuvant chemotherapy FIRST → mastectomy → radiation (surgery first is contraindicated)", "choices": ["Neoadjuvant chemotherapy FIRST → mastectomy → radiation (surgery first is contraindicated)", "Immediate mastectomy then chemotherapy", "Lumpectomy + radiation only", "Radiation then mastectomy"], "explanation": "IBC treatment: NACT (neoadjuvant chemotherapy) first to control systemic disease and downstage; modified radical mastectomy; then post-mastectomy radiation to the chest wall and regional nodes. BCS is contraindicated for IBC. Immediate surgery without NACT leads to very high local recurrence. IBC has the worst prognosis of all breast cancer subtypes (5-year OS ~30–40% without optimal treatment)."},
{"id": 183, "cat": "Breast/Pregnancy", "q": "A 29-year-old woman at 20 weeks gestation is found to have a 2 cm ER+/HER2− invasive ductal carcinoma. What is the safest treatment approach?", "source": "Breast Cancer in Pregnancy Guidelines", "correct": "Surgery (lumpectomy or mastectomy) in 2nd/3rd trimester; delay radiation and endocrine therapy until after delivery; chemotherapy acceptable after 14 weeks", "choices": ["Surgery (lumpectomy or mastectomy) in 2nd/3rd trimester; delay radiation and endocrine therapy until after delivery; chemotherapy acceptable after 14 weeks", "Delay all treatment until after delivery", "Termination of pregnancy required before treatment", "Radiation therapy safe throughout all trimesters"], "explanation": "Breast cancer in pregnancy: surgery is safe in 2nd and 3rd trimesters. Chemotherapy (AC regimen) is safe after 14 weeks (organogenesis complete). Radiation is contraindicated during pregnancy (fetal risk). Tamoxifen/aromatase inhibitors are teratogenic → delay until post-delivery. Sentinel lymph node biopsy with blue dye is relatively contraindicated (patent blue V); technetium-99m is acceptable."},
{"id": 184, "cat": "Breast/Pregnancy", "q": "Paget's disease of the breast presents as eczematoid nipple changes. What is the underlying malignancy in >95% of cases?", "source": "Breast Surgery / Paget's Disease", "correct": "Underlying DCIS or invasive carcinoma of the breast", "choices": ["Underlying DCIS or invasive carcinoma of the breast", "Primary skin malignancy (extramammary Paget's)", "Benign nipple eczema", "Nipple adenoma only"], "explanation": "Paget's disease of the breast: Paget cells (large, pale, intraepidermal adenocarcinoma cells) in the nipple epidermis represent spread from underlying ductal carcinoma in situ (DCIS) or invasive carcinoma. >95% have underlying breast malignancy (often central, sometimes non-palpable). Work-up: core biopsy of nipple, bilateral mammogram, MRI if mammogram negative. Treatment: lumpectomy (nipple included) or mastectomy depending on extent."},
{"id": 185, "cat": "Breast/Pregnancy", "q": "A 35-year-old woman has a 3 cm phyllodes tumor resected. Pathology shows pushing borders, 4 mitoses/10 HPF, and mild stromal cellularity. What is the classification and recommended margin?", "source": "Breast Surgery / Phyllodes Tumor", "correct": "Borderline phyllodes; wide local excision with ≥1 cm margins", "choices": ["Borderline phyllodes; wide local excision with ≥1 cm margins", "Benign phyllodes; enucleation sufficient", "Malignant phyllodes; mastectomy required", "Benign phyllodes; lumpectomy with close margins acceptable"], "explanation": "Phyllodes tumor classification: Benign (1–3 mitoses/10HPF, no atypia, pushing margins) → wide excision ≥1 cm; Borderline (4–9 mitoses, mild atypia); Malignant (≥10 mitoses/10HPF, severe atypia, infiltrative borders) → wide excision ≥1 cm (mastectomy if inadequate margins achievable). Phyllodes is a fibroepithelial stromal tumor; recurrence relates to margins, NOT benign/borderline/malignant classification alone. No sentinel node biopsy (rarely metastasizes to nodes)."},
{"id": 186, "cat": "Breast/Pregnancy", "q": "Male breast cancer accounts for ~1% of all breast cancers. What is the most common histologic subtype and receptor status?", "source": "Male Breast Cancer / NCCN", "correct": "Invasive ductal carcinoma, ER+ (~90%)", "choices": ["Invasive ductal carcinoma, ER+ (~90%)", "Triple-negative; ER−/PR−/HER2−", "HER2-amplified invasive ductal carcinoma", "Lobular carcinoma, ER+"], "explanation": "Male breast cancer: ~90% invasive ductal carcinoma, ~90% ER-positive. BRCA2 mutation is the most common genetic risk factor in men (lifetime risk 6–7% vs 0.1% population). Treatment: modified radical mastectomy (BCS possible but rarely performed), adjuvant tamoxifen (AI less effective due to residual aromatase in males). SLNB for staging. Lobular carcinoma is rare in men (<2%)."},
{"id": 187, "cat": "Breast/Pregnancy", "q": "Spontaneous unilateral bloody nipple discharge is most commonly caused by which benign lesion, and what is the management?", "source": "Breast Surgery / Nipple Discharge", "correct": "Intraductal papilloma; duct excision (microdochectomy) for diagnosis and treatment", "choices": ["Intraductal papilloma; duct excision (microdochectomy) for diagnosis and treatment", "Breast cancer; mastectomy", "Fibrocystic change; observe", "Ductal ectasia; antibiotics"], "explanation": "Unilateral, spontaneous, bloody/blood-tinged nipple discharge from a single duct: most common cause is intraductal papilloma (benign; small papillary growth within a lactiferous duct). Malignancy accounts for ~5–15%. Work-up: mammogram, ultrasound, ductoscopy. Management: major duct excision (microdochectomy) to obtain histology and treat. Bilateral, multiductal, spontaneous milky/cloudy discharge → evaluate for hyperprolactinemia."},
{"id": 188, "cat": "Breast/Pregnancy", "q": "The Z0011 trial (ACOSOG) demonstrated which major change in axillary management for early-stage breast cancer?", "source": "ACOSOG Z0011 Trial", "correct": "1–2 positive sentinel lymph nodes in early-stage BC treated with BCS + whole-breast radiation do NOT require completion ALND", "choices": ["1–2 positive sentinel lymph nodes in early-stage BC treated with BCS + whole-breast radiation do NOT require completion ALND", "Sentinel lymph node biopsy is no longer needed", "ALND is required for all node-positive disease", "3 or more positive sentinel nodes still require ALND"], "explanation": "Z0011: patients with cT1-2 N0 breast cancer treated with BCS + adjuvant systemic therapy + whole-breast radiation with 1–2 positive SLNs had equivalent OS and DFS whether they had completion ALND or not. ALND avoided unnecessary morbidity (lymphedema, shoulder dysfunction). Criteria: BCS (NOT mastectomy), 1–2 SLN+, whole-breast (not partial) RT, adjuvant systemic therapy."},
{"id": 76, "cat": "General", "q": "During a pancreaticoduodenectomy (Whipple procedure), which structure is NOT resected?", "source": "PSGS Review 2026", "correct": "Body and tail of the pancreas", "choices": ["Body and tail of the pancreas", "Head and neck of the pancreas", "Distal common bile duct", "Second and third portions of the duodenum"], "explanation": "Classic Whipple (pancreaticoduodenectomy) resects: pancreatic head/neck, entire duodenum, distal stomach (antrectomy), gallbladder, distal CBD, and regional lymph nodes. Body and tail of pancreas are preserved (along with the spleen in a classic Whipple). Pylorus-preserving PD (PPPD) retains the pylorus and first 2cm of duodenum to reduce dumping/ulcer but may increase delayed gastric emptying."},
{"id": 77, "cat": "General", "q": "A Hartmann procedure is most commonly indicated for:", "source": "ASCRS Guidelines 2022", "correct": "Perforated diverticulitis with fecal peritonitis (Hinchey III/IV) in unstable patients", "choices": ["Perforated diverticulitis with fecal peritonitis (Hinchey III/IV) in unstable patients", "Uncomplicated sigmoid diverticulitis refractory to antibiotics", "Obstructing left-sided colon cancer in an elective setting", "Ischemic colitis limited to the sigmoid colon"], "explanation": "Hartmann procedure: resects the sigmoid colon → end colostomy + closed rectal stump. Classic indication: perforated diverticulitis (Hinchey III-IV) or obstructed unprepared left colon in unstable patients. Avoids anastomosis in contaminated/unprepared bowel. Reversal is possible but carries ~50% major complication rate, so many patients remain with permanent colostomy."},
{"id": 78, "cat": "General", "q": "Hinchey Class III diverticulitis (purulent peritonitis) is primarily managed with:", "source": "ASCRS Guidelines 2022", "correct": "Urgent surgery — lavage ± Hartmann (or primary anastomosis with defunctioning stoma)", "choices": ["Urgent surgery — lavage ± Hartmann (or primary anastomosis with defunctioning stoma)", "IV antibiotics and CT-guided percutaneous drainage", "IV antibiotics alone — no drainage needed", "Elective sigmoid colectomy after 6 weeks of antibiotics"], "explanation": "Hinchey classification: I=pericolic abscess; II=pelvic/distant abscess; III=purulent peritonitis (generalized); IV=fecal peritonitis. I-II: IV antibiotics ± percutaneous drain. III: urgent surgery (laparoscopic peritoneal lavage/washout is an option in select patients, or Hartmann/primary anastomosis). IV: Hartmann is preferred — primary anastomosis very high risk in fecal contamination."},
{"id": 79, "cat": "General", "q": "The most critical technical factor for anastomotic healing (and the most important modifiable cause of anastomotic leak) is:", "source": "PSGS Review 2026", "correct": "Adequate blood supply (ischemia is the leading technical cause of anastomotic leak)", "choices": ["Adequate blood supply (ischemia is the leading technical cause of anastomotic leak)", "Absence of tension on the anastomosis", "Mechanical bowel preparation before surgery", "Use of stapled rather than hand-sewn technique"], "explanation": "Anastomotic leak causes: ischemia (most important technical factor), tension, contamination, poor technique. Patient factors: malnutrition, steroids, diabetes, obesity, radiation, emergency setting. Ischemia is the leading technical cause and is often preventable (ensure mesenteric vessel preservation, avoid devascularization, tension-free and well-perfused anastomosis). Leak typically presents day 5-7."},
{"id": 80, "cat": "General", "q": "In the FAST examination, which window is MOST sensitive for detecting hemoperitoneum?", "source": "ATLS 10th Ed. / PSGS Trauma", "correct": "Right upper quadrant / Morrison's pouch (hepatorenal space)", "choices": ["Right upper quadrant / Morrison's pouch (hepatorenal space)", "Left upper quadrant / splenorenal space", "Pelvic / pouch of Douglas", "Pericardial / subxiphoid window"], "explanation": "Morrison's pouch (hepatorenal space, RUQ) is the most dependent peritoneal space in the supine patient and the most sensitive single window for detecting free intraperitoneal fluid. As little as 200-250 mL of blood may be detectable here. The eFAST adds bilateral lung views to detect pneumothorax (loss of lung sliding)."},
{"id": 81, "cat": "General", "q": "Damage control surgery Phase 2 is primarily focused on:", "source": "ATLS 10th Ed.", "correct": "ICU resuscitation — correcting the lethal triad (hypothermia, acidosis, coagulopathy)", "choices": ["ICU resuscitation — correcting the lethal triad (hypothermia, acidosis, coagulopathy)", "Definitive surgical repair of all injuries", "Abbreviated laparotomy for hemorrhage control and contamination control", "Re-exploration and bowel anastomosis"], "explanation": "Damage control surgery phases: Phase 1 (OR) = abbreviated surgery: control hemorrhage (packing/vascular control), control contamination (staple bowel, do NOT anastomose), temporary abdominal closure (VAC/Bogota). Phase 2 (ICU) = aggressive resuscitation: warm fluids, correct coagulopathy (FFP/platelets), reverse acidosis. Phase 3 (OR, 24-72h) = definitive repair, bowel anastomosis, fascial closure."},
{"id": 82, "cat": "General", "q": "The 'lethal triad' in major trauma consists of:", "source": "ATLS 10th Ed.", "correct": "Hypothermia + Acidosis + Coagulopathy", "choices": ["Hypothermia + Acidosis + Coagulopathy", "Hypoxia + Hypotension + Hypothermia", "Tachycardia + Acidosis + Coagulopathy", "Hypocalcemia + Hypothermia + Hyponatremia"], "explanation": "Lethal triad: (1) Hypothermia (<35°C) → impairs clotting factors; (2) Acidosis (pH <7.35) → worsens coagulopathy; (3) Coagulopathy (INR >1.5) → ongoing hemorrhage. They are mutually reinforcing — each worsens the others. Prevention: damage control resuscitation with 1:1:1 (PRBCs:FFP:Platelets), permissive hypotension (SBP 80-90 penetrating, 90-100 TBI), warm blood products, avoid crystalloid overload."},
{"id": 83, "cat": "General", "q": "A Child-Pugh score of 7 corresponds to class:", "source": "EASL Guidelines", "correct": "Child-Pugh class B (7-9 = significant dysfunction)", "choices": ["Child-Pugh class B (7-9 = significant dysfunction)", "Child-Pugh class A (5-6 = well-compensated)", "Child-Pugh class C (10-15 = decompensated)", "No Child-Pugh class — score of 7 is borderline normal"], "explanation": "Child-Pugh scoring: A=5-6 (well-compensated, surgical risk acceptable); B=7-9 (significant dysfunction, increased surgical risk); C=10-15 (decompensated, most major resections contraindicated). Scored on: bilirubin, albumin, PT/INR, ascites, encephalopathy (1-3 points each). Child-Pugh C = relative contraindication to major hepatic resection."},
{"id": 84, "cat": "General", "q": "At what MELD score does liver transplantation confer a survival advantage over medical management?", "source": "AASLD / EASL Guidelines", "correct": "MELD ≥ 15", "choices": ["MELD ≥ 15", "MELD ≥ 25", "MELD ≥ 10", "MELD ≥ 20"], "explanation": "MELD (Model for End-Stage Liver Disease) = 3.78(ln bilirubin) + 11.2(ln INR) + 9.57(ln creatinine) + 6.43. Range 6-40. MELD ≥15: transplant survival benefit exceeds medical management → listing threshold. UNOS organ allocation uses MELD (sickest first, highest MELD). MELD-Na incorporates sodium for hyponatremia-associated mortality risk."},
{"id": 85, "cat": "General", "q": "In massive transfusion for hemorrhagic shock, the 1:1:1 ratio refers to:", "source": "ATLS / Damage Control Resuscitation", "correct": "1 unit PRBCs : 1 unit FFP : 1 unit platelets (damage control resuscitation)", "choices": ["1 unit PRBCs : 1 unit FFP : 1 unit platelets (damage control resuscitation)", "1 unit PRBCs : 1 unit cryoprecipitate : 1 unit FFP", "1 unit PRBCs : 1 unit albumin : 1 unit platelets", "1 unit PRBCs : 1 unit normal saline : 1 unit FFP"], "explanation": "Damage control resuscitation (DCR): transfuse PRBCs:FFP:Platelets in 1:1:1 ratio to approximate whole blood. Minimizes coagulopathy, dilutional effects, and hypothermia from crystalloids. Permissive hypotension (SBP 80-90 in penetrating trauma; 90-100 in TBI) until surgical hemorrhage control. Add tranexamic acid (TXA) within 3 hours of injury to reduce fibrinolysis."},
{"id": 194, "cat": "General", "q": "A patient develops a surgical site infection (SSI) 5 days after appendectomy. The wound is erythematous, warm, and fluctuant. What is the most important management step?", "source": "SSI Management / CDC Guidelines", "correct": "Open and drain the wound (incision and drainage)", "choices": ["Open and drain the wound (incision and drainage)", "IV antibiotics alone", "Oral antibiotics and observation", "Wound vacuum therapy immediately"], "explanation": "SSI with fluctuance = abscess = requires I&D. Opening the wound (incision and drainage + wet-to-dry dressing changes) is the primary treatment. Antibiotics alone cannot penetrate an organized abscess. Antibiotics are added if: surrounding cellulitis >2 cm, systemic signs of infection, immunocompromised patient. Wound VAC after wound is clean and granulating, not as initial treatment."},
{"id": 195, "cat": "General", "q": "A seroma develops 2 weeks after inguinal hernia repair. The patient has no fever, normal WBC, and minimal discomfort. What is the most appropriate management?", "source": "Hernia Surgery / Seroma Management", "correct": "Observation — most seromas resolve spontaneously within 6–8 weeks", "choices": ["Observation — most seromas resolve spontaneously within 6–8 weeks", "Immediate aspiration", "Surgical drainage", "IV antibiotics empirically"], "explanation": "Seromas (fluid collections in dead space after surgery) are very common after hernia repair, especially large hernias or mesh repairs. Management: observation for asymptomatic or mildly symptomatic seromas — >90% resolve within 6–8 weeks. Aspiration only for large/uncomfortable seromas (risk of introducing infection with each aspiration). Seroma ≠ SSI (no fever, erythema, or purulence). Key: reassure the patient."},
{"id": 196, "cat": "General", "q": "A patient with a Hartmann's procedure for perforated sigmoid diverticulitis is considered for reversal 3 months later. Prior to Hartmann's reversal, which preoperative step is most important?", "source": "Colorectal Surgery / Hartmann's Reversal", "correct": "Rigid sigmoidoscopy or contrast enema to assess rectal stump length and patency", "choices": ["Rigid sigmoidoscopy or contrast enema to assess rectal stump length and patency", "Routine colonoscopy of the colon only", "CT scan of abdomen is sufficient", "No additional workup needed if patient is asymptomatic"], "explanation": "Before Hartmann's reversal: assess rectal stump with rigid sigmoidoscopy or Gastrografin enema to: (1) confirm stump viability, (2) measure stump length (determines feasibility of colorectal anastomosis), (3) exclude stricture or fistula. A very short rectal stump may require coloanal anastomosis or permanent colostomy. CT scan cannot adequately assess stump length or luminally."},
{"id": 197, "cat": "General", "q": "During a Whipple procedure, the surgeon ligates the gastroduodenal artery (GDA). Which major vessel does the GDA arise from?", "source": "Vascular Anatomy / GDA", "correct": "Common hepatic artery", "choices": ["Common hepatic artery", "Superior mesenteric artery", "Celiac trunk (directly)", "Right hepatic artery"], "explanation": "The GDA arises from the common hepatic artery (branch of celiac trunk). Sequence: celiac trunk → common hepatic artery → GDA (downward) + proper hepatic artery (continues to liver). The GDA gives the superior pancreaticoduodenal arteries. During Whipple, the GDA is divided; the proper hepatic artery must be preserved. An aberrant right hepatic artery from the SMA is present in ~15–20% and must be identified."},
{"id": 198, "cat": "General", "q": "A patient is undergoing bowel preparation for elective colon surgery. Which combination constitutes the current enhanced recovery after surgery (ERAS) protocol recommendation?", "source": "ERAS Society Guidelines / Colorectal", "correct": "Oral mechanical bowel prep + oral antibiotics (combined reduces SSI without increasing complications)", "choices": ["Oral mechanical bowel prep + oral antibiotics (combined reduces SSI without increasing complications)", "Mechanical bowel prep alone (oral antibiotics add no benefit)", "No bowel prep required for elective colectomy", "Enema alone, no oral prep"], "explanation": "ERAS colorectal guidelines: combined oral mechanical bowel preparation (polyethylene glycol) + oral antibiotics (neomycin + metronidazole or neomycin + erythromycin) reduces surgical site infection rates (by 50–70%) compared to mechanical prep alone. MBP alone (without oral antibiotics) does not reduce SSI compared to no prep. Current evidence: combination prep is superior; some high-volume centers use oral antibiotics alone."},
{"id": 63, "cat": "Hereditary", "q": "BRCA1-associated breast cancers most commonly display which receptor profile?", "source": "NCCN Hereditary Breast/Ovarian v1.2025", "correct": "Triple-negative (ER-, PR-, HER2-)", "choices": ["Triple-negative (ER-, PR-, HER2-)", "ER-positive, PR-positive, HER2-negative", "HER2-positive", "Luminal A (ER+, low Ki67)"], "explanation": "BRCA1-associated breast cancers are often high-grade, ER-negative, PR-negative, HER2-negative (triple-negative, TNBC). BRCA2-associated cancers tend to be ER-positive and are more similar to sporadic breast cancers. Knowing this helps guide systemic therapy (PARP inhibitors effective in BRCA-mutated TNBC)."},
{"id": 64, "cat": "Hereditary", "q": "After colorectal cancer, what is the second most common malignancy in Lynch syndrome?", "source": "NCCN Colorectal v1.2025", "correct": "Endometrial cancer", "choices": ["Endometrial cancer", "Ovarian cancer", "Gastric cancer", "Urothelial/bladder cancer"], "explanation": "Lynch syndrome (MMR gene mutations: MLH1, MSH2, MSH6, PMS2): (1) CRC — most common; (2) Endometrial cancer — second most common (up to 40-60% lifetime risk with MSH2/MLH1 mutations). Ovarian, gastric, urothelial, small bowel, and pancreatic cancers also elevated. Lynch-associated endometrial cancer often presents before age 50."},
{"id": 65, "cat": "Hereditary", "q": "Without prophylactic colectomy, FAP patients have what lifetime risk of colorectal cancer by age 40-50?", "source": "NCCN Colorectal v1.2025", "correct": "Virtually 100%", "choices": ["Virtually 100%", "60-70%", "40-50%", "25-30%"], "explanation": "FAP = APC gene (chromosome 5q21). Hundreds to thousands of adenomatous polyps carpet the colon by the 2nd-3rd decade. Without prophylactic colectomy, virtually 100% develop CRC by age 40-50. Prophylactic proctocolectomy or colectomy with IRA recommended by age 20-25. Attenuated FAP (AFAP) = <100 polyps, later onset, lower (but still high) CRC risk."},
{"id": 66, "cat": "Hereditary", "q": "Cowden syndrome (PTEN mutation) is associated with which thyroid cancer histology?", "source": "NCCN Thyroid v1.2025", "correct": "Follicular thyroid carcinoma (NOT papillary)", "choices": ["Follicular thyroid carcinoma (NOT papillary)", "Papillary thyroid carcinoma", "Medullary thyroid carcinoma", "Anaplastic thyroid carcinoma"], "explanation": "Cowden syndrome (PTEN gene, 10q23): hamartomas throughout GI tract, trichilemmomas (pathognomonic facial lesions), macrocephaly. Cancers: breast (25-50%), thyroid (follicular — specifically follicular, NOT papillary), endometrial. Key distinction: when a hereditary syndrome question asks about thyroid cancer with PTEN, the answer is follicular carcinoma."},
{"id": 67, "cat": "Hereditary", "q": "A TP53 mutation (Li-Fraumeni syndrome) patient requires treatment for breast cancer. The treatment most important to AVOID is:", "source": "NCCN Li-Fraumeni / ASCO", "correct": "Radiation therapy", "choices": ["Radiation therapy", "Anthracycline chemotherapy", "Taxane chemotherapy", "Hormonal therapy (tamoxifen)"], "explanation": "Li-Fraumeni (TP53): patients have germline loss of p53 tumor suppressor → inability to undergo apoptosis in response to DNA damage. Radiation therapy induces DNA damage → dramatically increases radiation-induced secondary malignancies. Avoid radiotherapy whenever possible. Standard chemotherapy (anthracyclines, taxanes) is still used. Annual whole-body MRI for surveillance."},
{"id": 68, "cat": "Hereditary", "q": "Von Hippel-Lindau (VHL) syndrome most commonly presents with which cancer?", "source": "NCCN Kidney v2.2025", "correct": "Clear cell renal cell carcinoma (bilateral and multifocal)", "choices": ["Clear cell renal cell carcinoma (bilateral and multifocal)", "Pheochromocytoma", "CNS hemangioblastoma", "Pancreatic neuroendocrine tumor"], "explanation": "VHL syndrome (VHL gene, 3p25): clear cell RCC (60-70%, bilateral/multifocal — most common cancer) + CNS/retinal hemangioblastomas + pheochromocytoma (bilateral 50%) + pancreatic cysts/NETs + endolymphatic sac tumors. Watch RCC lesions <3cm; resect when 3cm threshold reached. MRI abdomen every 2 years from age 15."},
{"id": 69, "cat": "Hereditary", "q": "Peutz-Jeghers syndrome causes mucocutaneous pigmentation most characteristically on the:", "source": "NCCN Colorectal v1.2025", "correct": "Lips, perioral skin, and buccal mucosa", "choices": ["Lips, perioral skin, and buccal mucosa", "Palms and soles only", "Trunk (café-au-lait spots)", "Eyelids and conjunctivae"], "explanation": "Peutz-Jeghers (STK11/LKB1 gene): hamartomatous GI polyps (small bowel > colon > stomach) + mucocutaneous pigmented macules on lips, perioral skin, and buccal mucosa (may fade with age). Cancer risks: GI, gynecologic (cervical/uterine), breast, pancreatic. Surveillance: EGD + colonoscopy starting age 8; MRI small bowel. Café-au-lait + axillary freckling = NF1."},
{"id": 70, "cat": "Hereditary", "q": "A family carries an HDGC (Hereditary Diffuse Gastric Cancer) CDH1 mutation. The recommended management is:", "source": "IGCLC Guidelines 2020", "correct": "Prophylactic total gastrectomy by age 20-30", "choices": ["Prophylactic total gastrectomy by age 20-30", "Annual EGD with systematic biopsies indefinitely", "Partial gastrectomy plus Billroth II reconstruction", "Prophylactic partial gastrectomy when surveillance biopsies show signet ring cells"], "explanation": "HDGC (CDH1/E-cadherin mutation): diffuse-type gastric cancer (signet ring cells) + lobular breast cancer. Surveillance biopsies often MISS early lesions (submucosal signet ring cells). Therefore, prophylactic TOTAL gastrectomy is recommended by age 20-30 (or 5 years younger than youngest affected family member). Annual breast MRI from age 30. Partial gastrectomy is NOT sufficient."},
{"id": 71, "cat": "Hereditary", "q": "Gardner syndrome is a variant of FAP distinguished by the presence of:", "source": "NCCN Colorectal v1.2025", "correct": "Osteomas, desmoid tumors, CHRPE, and cutaneous fibromas, in addition to colonic polyposis", "choices": ["Osteomas, desmoid tumors, CHRPE, and cutaneous fibromas, in addition to colonic polyposis", "Medulloblastoma in addition to colonic polyposis (Turcot variant)", "Hamartomatous polyps and mucocutaneous pigmentation", "Juvenile polyps and arteriovenous malformations"], "explanation": "Gardner syndrome = FAP + extracolonic manifestations: osteomas (mandible), desmoid tumors (mesentery, often after surgery), congenital hypertrophy of retinal pigment epithelium (CHRPE, pathognomonic on fundoscopy), cutaneous fibromas, epidermoid cysts, supernumerary teeth. All are APC gene mutations. Turcot = FAP + medulloblastoma (or Lynch + glioblastoma)."},
{"id": 72, "cat": "Hereditary", "q": "MUTYH-associated polyposis (MAP) differs from all other polyposis syndromes because it is:", "source": "NCCN Colorectal v1.2025", "correct": "Autosomal recessive (requires biallelic MUTYH mutations)", "choices": ["Autosomal recessive (requires biallelic MUTYH mutations)", "X-linked dominant (affects mostly females)", "Autosomal dominant with variable penetrance", "Caused by a de novo mutation (not inherited)"], "explanation": "MAP = MUTYH gene (base excision repair pathway). Unique among polyposis syndromes: autosomal RECESSIVE — both alleles must be mutated. Phenotype: 10-100 polyps (attenuated FAP-like), CRC risk ~43% by age 60, duodenal polyps. Distinguish from FAP by negative APC testing and positive biallelic MUTYH testing. Colonoscopy q2yr; consider prophylactic colectomy."},
{"id": 73, "cat": "Hereditary", "q": "The hallmark finding of Neurofibromatosis type 2 (NF2) that distinguishes it from NF1 is:", "source": "NF Clinical Guidelines", "correct": "Bilateral vestibular schwannomas (acoustic neuromas)", "choices": ["Bilateral vestibular schwannomas (acoustic neuromas)", "More than 6 café-au-lait macules (>15mm diameter)", "Plexiform neurofibromas pathognomonic of the condition", "Optic pathway gliomas in children"], "explanation": "NF2 (Merlin gene, 22q12): bilateral vestibular schwannomas = diagnostic hallmark (causing bilateral hearing loss/tinnitus). Also: multiple meningiomas, spinal schwannomas, cataracts. NF1 (17q11): café-au-lait spots, axillary/inguinal freckling, Lisch nodules, plexiform neurofibromas (pathognomonic), optic gliomas, MPNSTs. NF1 = much more common, also known as von Recklinghausen's disease."},
{"id": 74, "cat": "Hereditary", "q": "Gorlin syndrome (Basal Cell Nevus Syndrome, PTCH1 mutation) patients should avoid which treatment for their malignancies?", "source": "NCCN BCC v1.2025", "correct": "Radiation therapy (causes massive BCC induction in the radiation field)", "choices": ["Radiation therapy (causes massive BCC induction in the radiation field)", "Hedgehog pathway inhibitors (vismodegib)", "Wide surgical excision with Mohs technique", "Topical imiquimod for superficial BCCs"], "explanation": "Gorlin syndrome (PTCH1, chromosome 9q22): multiple BCCs appearing by age 20, odontogenic keratocysts, bifid ribs, calcified falx cerebri, desmoplastic medulloblastoma. Critical: AVOID RADIATION — the PTCH1/hedgehog pathway mutation makes tissue exquisitely sensitive to radiation-induced carcinogenesis (massive BCC induction). Paradoxically, vismodegib (hedgehog inhibitor) IS used therapeutically in Gorlin syndrome."},
{"id": 75, "cat": "Hereditary", "q": "A newborn is found to have café-au-lait spots, and genetic testing confirms NF1. The most serious long-term malignancy risk is:", "source": "NF Clinical Guidelines", "correct": "Malignant peripheral nerve sheath tumor (MPNST)", "choices": ["Malignant peripheral nerve sheath tumor (MPNST)", "Glioblastoma multiforme", "Neuroblastoma", "Ependymoma"], "explanation": "NF1 lifetime cancer risk includes: MPNST (10% lifetime — transformation of plexiform neurofibroma, poor prognosis), optic gliomas (in children), brain tumors, leukemia, pheochromocytoma, GI stromal tumors (GIST). MPNST = the most feared malignant complication. Rapid growth or pain in a plexiform neurofibroma → suspect malignant transformation → MRI/biopsy."},
{"id": 209, "cat": "Hereditary", "q": "Familial adenomatous polyposis (FAP) is caused by an APC mutation. Which extracolonic manifestation carries the highest mortality in FAP patients after prophylactic colectomy?", "source": "FAP / Extracolonic Manifestations", "correct": "Duodenal/periampullary adenocarcinoma (2nd most common cancer in FAP; lifetime risk ~5–10%)", "choices": ["Duodenal/periampullary adenocarcinoma (2nd most common cancer in FAP; lifetime risk ~5–10%)", "Thyroid cancer", "Desmoid tumor rupture", "Brain tumors (Turcot syndrome)"], "explanation": "FAP extracolonic manifestations: gastric polyps (fundic gland, usually benign), duodenal adenomas (Spigelman classification; grade IV → prophylactic surgery), periampullary carcinoma (lifetime risk 5–10%, 2nd leading cause of death in FAP after CRC), desmoid tumors (Gardner syndrome), osteomas, CHRPE (congenital hypertrophy of retinal pigment epithelium), epidermoid cysts. Upper GI surveillance with forward-viewing + side-viewing endoscopy every 1–3 years starting at age 25."},
{"id": 210, "cat": "Hereditary", "q": "Lynch syndrome (hereditary non-polyposis colorectal cancer) is caused by mutations in mismatch repair genes. Which gene mutation is most common in Lynch syndrome, and what is the colonic phenotype?", "source": "Lynch Syndrome / HNPCC", "correct": "MLH1 (most common, ~40%); few to no polyps, proximal/right-sided colon cancers, microsatellite instability-high", "choices": ["MLH1 (most common, ~40%); few to no polyps, proximal/right-sided colon cancers, microsatellite instability-high", "APC; hundreds of adenomatous polyps throughout colon", "BRCA2; predominantly left-sided cancers", "SMAD4; numerous hamartomatous polyps"], "explanation": "Lynch syndrome: MMR gene mutations (MLH1, MSH2, MSH6, PMS2); MLH1 most common. Phenotype: few to no polyps (unlike FAP), right-sided/proximal colon preference (70%), MSI-H tumors (associated with better prognosis, responsive to immunotherapy). Amsterdam II criteria: 3-2-1 rule. Surveillance: colonoscopy every 1–2 years starting age 20–25. Extracolonic: endometrial, ovarian, stomach, urinary tract, pancreatic cancers."},
{"id": 1, "cat": "Hernia", "q": "What are the three borders of Hesselbach's triangle?", "source": "PSGS Review 2026", "correct": "Rectus sheath (medial), inguinal ligament (inferior), inferior epigastric vessels (lateral)", "choices": ["Rectus sheath (medial), inguinal ligament (inferior), inferior epigastric vessels (lateral)", "Pubic tubercle (medial), Cooper's ligament (inferior), femoral vessels (lateral)", "Linea alba (medial), arcuate line (inferior), inferior epigastric vessels (lateral)", "Rectus sheath (medial), inguinal ligament (inferior), external iliac vessels (lateral)"], "explanation": "Hesselbach's triangle: medial = lateral edge of rectus sheath; inferior = inguinal ligament; lateral = inferior epigastric vessels. Direct hernias protrude through this triangle."},
{"id": 2, "cat": "Hernia", "q": "Which type of inguinal hernia passes lateral to the inferior epigastric vessels and may descend into the scrotum?", "source": "PSGS Review 2026", "correct": "Indirect hernia", "choices": ["Indirect hernia", "Direct hernia", "Femoral hernia", "Spigelian hernia"], "explanation": "Indirect hernias pass through the deep (internal) inguinal ring, lateral to the inferior epigastric vessels, and can travel through the inguinal canal into the scrotum. Direct hernias pass medially through Hesselbach's triangle and do not typically enter the scrotum."},
{"id": 3, "cat": "Hernia", "q": "Using the NAVEL mnemonic (medial→lateral), what occupies the femoral canal?", "source": "PSGS Review 2026", "correct": "The empty space (E) — the femoral canal itself contains lymphatics", "choices": ["The empty space (E) — the femoral canal itself contains lymphatics", "The femoral nerve (N) — the most medial structure", "The femoral artery (A) — the central landmark", "The femoral vein (V) — the most medial structure"], "explanation": "NAVEL from medial to lateral: Nerve, Artery, Vein, Empty space (canal), Lymphatics. The femoral canal = the 'E' — it's the medial compartment of the femoral sheath, containing fat and lymphatics. Femoral hernias protrude through this empty space."},
{"id": 4, "cat": "Hernia", "q": "What is the gold standard open repair for inguinal hernia?", "source": "SAGES Guidelines", "correct": "Lichtenstein tension-free mesh repair", "choices": ["Lichtenstein tension-free mesh repair", "Shouldice repair (four-layer fascial repair)", "McVay (Cooper's ligament) repair", "Bassini repair"], "explanation": "The Lichtenstein tension-free mesh repair is the gold standard open repair with recurrence rates <1%. It places a polypropylene mesh over the posterior inguinal wall. Shouldice has low recurrence without mesh but is technically demanding. McVay is reserved for femoral hernias."},
{"id": 5, "cat": "Hernia", "q": "In laparoscopic inguinal hernia repair, which approach avoids entering the peritoneal cavity entirely?", "source": "SAGES Guidelines", "correct": "TEP (Totally ExtraPeritoneal)", "choices": ["TEP (Totally ExtraPeritoneal)", "TAPP (TransAbdominal PrePeritoneal)", "IPOM (IntraPeritoneal Onlay Mesh)", "Stoppa repair"], "explanation": "TEP = Totally ExtraPeritoneal — the peritoneum is never entered, reducing bowel injury risk. TAPP = TransAbdominal PrePeritoneal — enters the peritoneal cavity first, then dissects the preperitoneal space. TAPP allows better visualization for bilateral hernias."},
{"id": 6, "cat": "Hernia", "q": "Which open inguinal hernia repair is the ONLY one that also addresses the femoral space?", "source": "PSGS Review 2026", "correct": "McVay repair (Cooper's ligament repair)", "choices": ["McVay repair (Cooper's ligament repair)", "Lichtenstein repair", "Shouldice repair", "TAPP repair"], "explanation": "The McVay repair sutures the transversalis fascia/conjoint tendon to Cooper's (pectineal) ligament. Because Cooper's ligament forms the posterior boundary of the femoral canal, this is the only traditional open repair that covers the femoral space. A relaxing incision is often needed to reduce tension."},
{"id": 7, "cat": "Hernia", "q": "A Richter's hernia is best described as:", "source": "PSGS Review 2026", "correct": "Only the antimesenteric wall of the bowel is incarcerated (no complete lumen obstruction)", "choices": ["Only the antimesenteric wall of the bowel is incarcerated (no complete lumen obstruction)", "A Meckel's diverticulum inside the hernia sac", "The appendix inside an inguinal hernia sac", "A W-loop of bowel with the intervening segment strangulated"], "explanation": "Richter's = partial circumference of bowel wall (antimesenteric side) is trapped. Because the lumen is not completely obstructed, bowel obstruction signs may be absent, making it easy to miss. Gangrene and perforation can still occur. Littre's = Meckel's diverticulum; Amyand's = appendix; Maydl's = W-loop."},
{"id": 8, "cat": "Hernia", "q": "Howship-Romberg sign — pain in the medial thigh/knee worsened by hip extension — is pathognomonic of which hernia?", "source": "PSGS Review 2026", "correct": "Obturator hernia", "choices": ["Obturator hernia", "Femoral hernia", "Spigelian hernia", "Lumbar hernia"], "explanation": "Obturator hernias pass through the obturator foramen and compress the obturator nerve, causing medial thigh or knee pain (Howship-Romberg sign). They predominantly occur in elderly thin multiparous women. Diagnosis by CT. High strangulation risk → surgical emergency."},
{"id": 9, "cat": "Hernia", "q": "Which is the more common lumbar hernia — Grynfeltt-Lesshaft or Petit's?", "source": "PSGS Review 2026", "correct": "Grynfeltt-Lesshaft (superior lumbar triangle)", "choices": ["Grynfeltt-Lesshaft (superior lumbar triangle)", "Petit's (inferior lumbar triangle)", "Both are equally common", "Neither — lumbar hernias always occur through the iliac crest"], "explanation": "Grynfeltt-Lesshaft (superior lumbar triangle: 12th rib, erector spinae, internal oblique) is more common than Petit's (inferior triangle: iliac crest, latissimus dorsi, external oblique). Both are typically acquired (post-trauma, post-surgical). CT confirms diagnosis."},
{"id": 10, "cat": "Hernia", "q": "In which hiatal hernia type does the gastroesophageal junction (GEJ) remain in the normal subdiaphragmatic position while the gastric fundus herniates?", "source": "SAGES Guidelines", "correct": "Type II (rolling/pure paraesophageal hernia)", "choices": ["Type II (rolling/pure paraesophageal hernia)", "Type I (sliding hernia)", "Type III (mixed hernia)", "Type IV (giant hernia with other organs)"], "explanation": "Type II = pure paraesophageal: GEJ stays below diaphragm (normal), but the fundus rolls up through the hiatus. Risk of organoaxial volvulus and strangulation — surgical repair is recommended even if asymptomatic. Type I (sliding) is the most common (95%) and involves GEJ displacement."},
{"id": 11, "cat": "Hernia", "q": "A 270° posterior partial fundoplication is called:", "source": "SAGES Guidelines", "correct": "Toupet fundoplication", "choices": ["Toupet fundoplication", "Nissen fundoplication", "Dor fundoplication", "Hill repair"], "explanation": "Toupet = 270° posterior partial wrap — used when esophageal peristalsis is weak (to reduce dysphagia). Nissen = 360° total wrap (highest efficacy, highest dysphagia risk, used with normal peristalsis). Dor = anterior 180° wrap (used after Heller myotomy for achalasia)."},
{"id": 12, "cat": "Hernia", "q": "Which test is MANDATORY before any anti-reflux surgery to rule out achalasia?", "source": "SAGES Guidelines", "correct": "Esophageal manometry", "choices": ["Esophageal manometry", "24-hour pH monitoring", "Upper GI barium swallow", "Esophagogastroduodenoscopy (EGD)"], "explanation": "Esophageal manometry is mandatory — wrapping around an achalasic esophagus will cause severe dysphagia. The full pre-op workup is: (1) UGI barium, (2) EGD, (3) 24-hr pH monitoring to confirm acid, (4) manometry to exclude achalasia and assess peristalsis to guide wrap choice."},
{"id": 13, "cat": "Hernia", "q": "Type 1 mesh (e.g., polypropylene) is characterized by:", "source": "PSGS Review 2026", "correct": "Large-pore (>75 μm) monofilament — best tissue ingrowth, lowest infection risk", "choices": ["Large-pore (>75 μm) monofilament — best tissue ingrowth, lowest infection risk", "Small-pore multifilament — highest tensile strength", "Non-permeable expanded PTFE film — for intraperitoneal placement", "Biologic acellular dermal matrix — for contaminated fields"], "explanation": "Type 1 mesh (e.g., Prolene/polypropylene) = large-pore monofilament → best tissue ingrowth and lowest infection risk → preferred for most repairs. Type 2 = small-pore (<10μm). Type 3 = multifilament small-pore (highest infection risk). Type 4 = non-permeable sheet (ePTFE, intraperitoneal use only)."},
{"id": 14, "cat": "Hernia", "q": "Biologic mesh should be used instead of synthetic mesh in which scenario?", "source": "PSGS Review 2026", "correct": "Contaminated/infected field (e.g., strangulated hernia with bowel resection)", "choices": ["Contaminated/infected field (e.g., strangulated hernia with bowel resection)", "All ventral hernia repairs in obese patients", "Any laparoscopic inguinal repair", "Recurrent hernias after prior mesh repair"], "explanation": "Biologic mesh (e.g., AlloDerm, Permacol) = acellular dermal matrix that allows tissue ingrowth and can be placed in contaminated fields. Indications: strangulated hernia, enterotomy, active infection (Class III-IV wound). Higher recurrence rate than synthetic but avoids chronic mesh infection risk."},
{"id": 15, "cat": "Hernia", "q": "The most common site for port-site hernia after laparoscopic surgery is:", "source": "PSGS Review 2026", "correct": "Umbilical port (midline, thin fascia, inadequate closure)", "choices": ["Umbilical port (midline, thin fascia, inadequate closure)", "Right lower quadrant 5mm port", "Epigastric 12mm port", "Left lateral 10mm port"], "explanation": "Port-site hernias most commonly occur at the umbilical trocar site because the midline fascial tissue is thinnest here and most prone to inadequate closure. Prevention: close fascia at ALL trocar sites ≥10mm. Presentation: bowel obstruction days-weeks post-operatively."},
{"id": 41, "cat": "Parathyroid", "q": "During parathyroidectomy, the Miami Criteria for cure requires the intraoperative PTH to:", "source": "AAES/ATA Guidelines 2022", "correct": "Drop >50% from the highest pre-excision level at 10 minutes post-excision", "choices": ["Drop >50% from the highest pre-excision level at 10 minutes post-excision", "Fall into the normal reference range regardless of percent drop", "Drop >50% from the baseline (pre-operative) level", "Decrease by at least 30 pg/mL in absolute terms"], "explanation": "Miami Criteria: PTH must drop >50% from the highest pre-excision value (intraoperative, not preoperative baseline) measured at 10 minutes after resection. If criteria are met → ~98% cure rate. If not met → residual parathyroid tissue remains → continue exploration. PTH half-life is ~3-5 minutes."},
{"id": 42, "cat": "Parathyroid", "q": "A patient has mild hypercalcemia and elevated PTH. The calcium-creatinine clearance ratio (CCCR) calculates to 0.008. This suggests:", "source": "AAES/ATA Guidelines 2022", "correct": "Familial Hypocalciuric Hypercalcemia (FHH) — do NOT operate", "choices": ["Familial Hypocalciuric Hypercalcemia (FHH) — do NOT operate", "Primary hyperparathyroidism — proceed with parathyroidectomy", "Secondary hyperparathyroidism from renal disease", "Tertiary hyperparathyroidism — 3.5-gland parathyroidectomy"], "explanation": "CCCR = (Urine Ca × Serum Cr) / (Serum Ca × Urine Cr). Interpretation: <0.01 = FHH (CaSR inactivating mutation — benign, lifelong hypercalcemia, DO NOT operate); >0.02 = PHPT (likely adenoma, operate if indicated); 0.01-0.02 = grey zone (send CaSR gene testing). FHH is autosomal dominant; surgery is not curative."},
{"id": 43, "cat": "Parathyroid", "q": "According to 2022 guidelines, which finding in an asymptomatic PHPT patient is an indication for parathyroidectomy?", "source": "AAES/ATA Guidelines 2022", "correct": "T-score ≤ -2.5 on DEXA at the lumbar spine", "choices": ["T-score ≤ -2.5 on DEXA at the lumbar spine", "Serum calcium 0.5 mg/dL above the upper limit of normal", "Patient age 60 years with no other criteria", "24-hour urine calcium of 350 mg/day without elevated stone risk"], "explanation": "2022 Indications for parathyroidectomy in asymptomatic PHPT (any 1 sufficient): Ca >1.0 mg/dL above ULN; age <50; T-score ≤-2.5 at any site OR vertebral fracture; 24hr urine Ca >400mg/day + elevated stone risk; CrCl <60 mL/min; nephrolithiasis/nephrocalcinosis; bone density loss >20% in 5 years. Ca only 0.5 above, age 60, urine Ca 350 — none meet criteria."},
{"id": 44, "cat": "Parathyroid", "q": "MEN1 syndrome is caused by a mutation in the MENIN gene located on chromosome 11q13. Which triad of organs is classically affected?", "source": "AAES/ATA Guidelines 2022", "correct": "Parathyroid (95%), Pituitary, Pancreatic NETs — the '3 P's'", "choices": ["Parathyroid (95%), Pituitary, Pancreatic NETs — the '3 P's'", "Pheo, Parathyroid, Papillary thyroid cancer", "Pancreas, Parathyroid, Peripheral nerve sheaths", "Pituitary, Pancreas, Prostate"], "explanation": "MEN1 = Menin gene (11q13), autosomal dominant. 3 P's: Parathyroid (most common, 95%), Pituitary (prolactinoma most common), Pancreatic NETs (gastrinoma → Zollinger-Ellison syndrome most common, also insulinoma, glucagonoma). Also associated with adrenal cortical tumors and carcinoids. Annual screening: PTH/Ca, prolactin, fasting glucose."},
{"id": 45, "cat": "Parathyroid", "q": "MEN2B is caused by a RET codon 918 mutation. Prophylactic thyroidectomy is recommended:", "source": "ATA Guidelines 2022", "correct": "Within 6 months of birth", "choices": ["Within 6 months of birth", "By age 5 years", "By age 10 years (puberty onset)", "When calcitonin levels first become elevated"], "explanation": "RET codon 918 = highest-risk mutation (MEN2B). MTC can develop in infancy — within the first 6 months of life. Therefore prophylactic thyroidectomy is recommended within 6 months of birth. MEN2B features: MTC + Pheo + Marfanoid habitus + mucosal neuromas (NO parathyroid disease). MEN2A (codon 634): thyroidectomy by age 5. Other mutations: guided by specific codon risk level."},
{"id": 46, "cat": "Parathyroid", "q": "Which feature MOST suggests parathyroid carcinoma rather than benign adenoma?", "source": "AAES/ATA Guidelines 2022", "correct": "Serum calcium >14 mg/dL with a palpable, rock-hard neck mass", "choices": ["Serum calcium >14 mg/dL with a palpable, rock-hard neck mass", "Bilateral parathyroid involvement", "Parathyroid gland weight >1 gram", "Sestamibi scan showing a single parathyroid adenoma"], "explanation": "Parathyroid carcinoma clues: Ca >14 mg/dL (often >16-17), PTH 3-5× ULN, palpable neck mass, 'stone hard' gland intraoperatively, adhesion/invasion to adjacent structures, RLN involvement. Pathology: Ki67 >5%, parafibromin loss (IHC), vascular/capsular invasion. Treatment: en bloc resection with ipsilateral thyroid lobe. Only ~1% of PHPT cases."},
{"id": 47, "cat": "Parathyroid", "q": "In the CHIMPANZEES mnemonic for hypercalcemia, what does the first 'H' represent?", "source": "AAES/ATA Guidelines 2022", "correct": "Hyperparathyroidism (primary) — most common cause", "choices": ["Hyperparathyroidism (primary) — most common cause", "Hypervitaminosis (excessive vitamin D)", "Hemolysis (in vitro artifact)", "Hypothyroidism (TSH-related calcium dysregulation)"], "explanation": "CHIMPANZEES: C=Ca supplements/thiazides, H=Hyperparathyroidism (primary, most common cause of outpatient hypercalcemia), I=Immobility/Iatrogenic, M=Milk-alkali, P=Paget's/Pheo, A=Addison's, N=Neoplasm (PTHrP-secreting tumor — most common cause of inpatient hypercalcemia), Z=ZE syndrome, E=Excess Vit D, E=Excess Vit A, S=Sarcoid/Syphilis."},
{"id": 48, "cat": "Parathyroid", "q": "Hungry bone syndrome after parathyroidectomy is characterized by:", "source": "AAES/ATA Guidelines 2022", "correct": "Severe hypocalcemia from rapid remineralization of bone depleted by chronic PTH excess", "choices": ["Severe hypocalcemia from rapid remineralization of bone depleted by chronic PTH excess", "Hyperphosphatemia from renal tubular dysfunction post-surgery", "Persistent hypercalcemia from residual parathyroid tissue", "Hypomagnesemia from intraoperative blood loss"], "explanation": "Hungry bone syndrome: after removing excess PTH, bones rapidly remineralize, consuming Ca (and Mg, PO4) from the blood → profound hypocalcemia. Risk factors: large preop Ca/PTH, osteitis fibrosa cystica, prolonged HPT, large resection. Treatment: aggressive IV Ca gluconate + high-dose oral calcium + calcitriol. Monitor Mg and K."},
{"id": 49, "cat": "Parathyroid", "q": "For a reoperative parathyroidectomy where sestamibi and ultrasound are non-concordant, the best next imaging modality is:", "source": "AAES/ATA Guidelines 2022", "correct": "4D-CT or PET-choline scan", "choices": ["4D-CT or PET-choline scan", "Repeat sestamibi with SPECT", "Invasive selective venous sampling", "MRI neck with gadolinium"], "explanation": "For reoperative cases with discordant first-line studies: 4D-CT provides detailed anatomic localization. PET-choline is emerging as the best modality for ectopic and multiglandular disease in reoperative cases. Selective venous sampling (SVS) is the gold standard when imaging fails but is invasive. First-line: sestamibi + neck U/S (if concordant → focused parathyroidectomy)."},
{"id": 50, "cat": "Parathyroid", "q": "The most common location for an ectopic inferior parathyroid gland is:", "source": "AAES/ATA Guidelines 2022", "correct": "Intrathymic (anterior mediastinum) — develops with thymus from 3rd pharyngeal pouch", "choices": ["Intrathymic (anterior mediastinum) — develops with thymus from 3rd pharyngeal pouch", "Retroesophageal — posterior mediastinum", "Carotid sheath — lateral neck", "Intrathyroidal — embedded within thyroid tissue"], "explanation": "Inferior parathyroids descend with the thymus from the 3rd pharyngeal pouch → most common ectopic location = intrathymic (anterior mediastinum). Treatment: cervical thymectomy usually suffices; VATS if deeper. Superior parathyroids (4th pouch) are more consistent in location — ectopic superiors go retroesophageal/retrolaryngeal. Most common cause of failed parathyroidectomy = missed ectopic gland."},
{"id": 199, "cat": "Parathyroid", "q": "A parathyroid carcinoma is suspected intraoperatively (hard, adherent to thyroid, dense scar). What is the correct surgical approach?", "source": "Parathyroid Carcinoma / Endocrine Surgery", "correct": "En-bloc resection including ipsilateral thyroid lobe and adherent structures (avoid capsular disruption)", "choices": ["En-bloc resection including ipsilateral thyroid lobe and adherent structures (avoid capsular disruption)", "Simple parathyroidectomy alone", "Biopsy only and refer for chemotherapy", "Bilateral neck exploration only"], "explanation": "Parathyroid carcinoma (~1% of PHPT): suspected when PTH markedly elevated (>3× ULN), palpable neck mass, serum calcium >14 mg/dL, or dense fibrous bands intraoperatively. Treatment: en-bloc resection with ipsilateral thyroid lobe + central compartment nodes, avoiding capsular disruption (seeding causes local recurrence). Frozen section unreliable. If capsular disruption occurs: reoperation is very difficult. Recurrence managed with more resection + denosumab/cinacalcet."},
{"id": 200, "cat": "Parathyroid", "q": "A patient on chronic hemodialysis develops secondary hyperparathyroidism with PTH of 1,800 pg/mL despite maximal medical therapy (cinacalcet, active vitamin D). Which surgical procedure is performed?", "source": "Secondary HPT Surgery", "correct": "Subtotal parathyroidectomy (3.5 glands) or total parathyroidectomy with autotransplantation", "choices": ["Subtotal parathyroidectomy (3.5 glands) or total parathyroidectomy with autotransplantation", "Single gland excision (minimal parathyroid surgery)", "Total thyroidectomy", "Medical management only; surgery not indicated"], "explanation": "Secondary HPT (renal failure): all 4 glands are hyperplastic. Surgery indicated when refractory to medical therapy (PTH >800 pg/mL, calciphylaxis, uncontrolled hypercalcemia/hyperphosphatemia). Two options: (1) Subtotal parathyroidectomy (remove 3.5 glands, leave remnant on well-vascularized pedicle); (2) Total parathyroidectomy + autotransplantation (non-dominant forearm). Mark the remnant/implant with clips for identification."},
{"id": 201, "cat": "Parathyroid", "q": "A patient undergoes successful renal transplantation after 10 years on dialysis. Six months post-transplant, serum calcium is 11.8 mg/dL and PTH is 380 pg/mL (high-normal). This is most consistent with:", "source": "Tertiary Hyperparathyroidism", "correct": "Tertiary hyperparathyroidism (autonomous PTH secretion despite restored renal function)", "choices": ["Tertiary hyperparathyroidism (autonomous PTH secretion despite restored renal function)", "Secondary hyperparathyroidism (expected to normalize)", "Primary hyperparathyroidism (coincidental adenoma)", "Hypercalcemia of malignancy"], "explanation": "Tertiary HPT: in long-standing secondary HPT, the hyperplastic parathyroid glands develop autonomous function (monoclonal nodular hyperplasia) — they no longer respond to calcium feedback. After renal transplant, PTH and calcium remain elevated. Management: cinacalcet first (6–12 months); if persistent hypercalcemia → parathyroidectomy (subtotal or total + AT). Distinguishing from primary HPT (adenoma) is difficult without prior history."},
{"id": 202, "cat": "Parathyroid", "q": "Intraoperative PTH monitoring (Miami criterion) during focused parathyroidectomy for primary hyperparathyroidism requires PTH to fall by what amount to confirm adequate resection?", "source": "Miami Criterion / IOPTH", "correct": ">50% drop from highest pre-excision PTH value, falling into the normal range, at 10 minutes post-resection", "choices": [">50% drop from highest pre-excision PTH value, falling into the normal range, at 10 minutes post-resection", ">25% drop from baseline", "PTH must reach zero", "PTH must drop below 10 pg/mL"], "explanation": "Miami criterion (Norman et al.): IOPTH drops >50% from the highest pre-excision level AND falls into the normal range (<65 pg/mL), measured at 10 minutes after gland removal. If criterion met → cure confirmed → focused operation complete. If not met → suggests multigland disease or missed adenoma → bilateral neck exploration. IOPTH has reduced failed operations and re-explorations significantly."},
{"id": 203, "cat": "Parathyroid", "q": "Familial hypocalciuric hypercalcemia (FHH) is an important mimic of primary hyperparathyroidism. Which finding distinguishes FHH from primary PHPT, and what is the treatment?", "source": "FHH vs PHPT Differentiation", "correct": "24-hour urine calcium-to-creatinine clearance ratio <0.01 (low urinary calcium); no treatment (surgery is NOT curative)", "choices": ["24-hour urine calcium-to-creatinine clearance ratio <0.01 (low urinary calcium); no treatment (surgery is NOT curative)", "Elevated PTH >500 pg/mL; treat with cinacalcet", "Nephrolithiasis and osteoporosis; parathyroidectomy curative", "High urinary calcium >400 mg/day; parathyroidectomy curative"], "explanation": "FHH: autosomal dominant inactivating mutation in calcium-sensing receptor (CaSR). Parathyroid glands require higher Ca to suppress PTH. Result: mild hypercalcemia + inappropriately normal/high PTH + very low urine Ca (UCCR <0.01). FHH is benign — no complications. Parathyroidectomy does NOT cure FHH (all glands affected). Must exclude FHH before operating for PHPT: calculate UCCR = (urine Ca × serum Cr)/(serum Ca × urine Cr)."},
{"id": 26, "cat": "Skin & STS", "q": "For a melanoma measuring 2.5 mm Breslow thickness, the recommended excision margin is:", "source": "NCCN Melanoma v2.2026", "correct": "2 cm", "choices": ["2 cm", "1 cm", "3 cm", "0.5 cm"], "explanation": "Melanoma margins by Breslow thickness: In situ → 0.5-1cm; <1mm → 1cm; 1-2mm → 1-2cm; >2mm → 2cm. For this 2.5mm tumor (>2mm), 2cm margins are required. Breslow thickness is the single most important prognostic factor."},
{"id": 27, "cat": "Skin & STS", "q": "Sentinel lymph node biopsy (SLNB) is recommended for melanoma when the Breslow thickness exceeds:", "source": "NCCN Melanoma v2.2026", "correct": "≥0.8 mm (or <0.8 mm with ulceration or other adverse features)", "choices": ["≥0.8 mm (or <0.8 mm with ulceration or other adverse features)", "Any melanoma regardless of thickness", ">1.0 mm Breslow thickness only", ">2.0 mm (T3) or above"], "explanation": "SLNB is indicated for Stage IB melanoma and above (NCCN 2026): (1) Breslow ≥0.8 mm with or without ulceration, OR (2) Breslow <0.8 mm WITH ulceration. SLNB is NOT indicated for Stage IA: Breslow <0.8 mm, non-ulcerated, no adverse features. If SLNB is positive → consider completion lymphadenectomy vs. nodal observation (per MSLT-II). Perform lymphatic mapping BEFORE wide excision to avoid disrupting lymphatics."},
{"id": 28, "cat": "Skin & STS", "q": "Merkel cell carcinoma is associated with which viral etiology?", "source": "NCCN MCC v1.2025", "correct": "Merkel cell polyomavirus (MCPyV)", "choices": ["Merkel cell polyomavirus (MCPyV)", "Human papillomavirus (HPV-16/18)", "Epstein-Barr virus (EBV)", "Human herpesvirus-8 (HHV-8/KSHV)"], "explanation": "Merkel cell carcinoma: ~80% associated with Merkel cell polyomavirus. It's an aggressive neuroendocrine skin tumor, CK20+ (paranuclear dot pattern), synaptophysin+, chromogranin+. Risk factors: UV exposure, immunosuppression, elderly. SLNB recommended for all. HHV-8 is associated with Kaposi sarcoma."},
{"id": 29, "cat": "Skin & STS", "q": "DFSP (Dermatofibrosarcoma Protuberans) characteristically stains positive for:", "source": "NCCN STS v2.2026", "correct": "CD34", "choices": ["CD34", "S-100", "CK20", "Desmin"], "explanation": "DFSP = CD34 positive. It is a low-grade fibroblastic sarcoma driven by a t(17;22) translocation creating COL1A1-PDGFR-β fusion. Low metastatic risk (<5%) but high local recurrence if margins inadequate. Treatment: Mohs surgery or wide excision 2-3cm. Imatinib for unresectable/metastatic disease (PDGFR-β targeted). S-100 = melanoma/nerve sheath; CK20 = Merkel cell; Desmin = muscle tumors."},
{"id": 30, "cat": "Skin & STS", "q": "For a 7 cm deep soft tissue mass in the thigh, the most appropriate biopsy technique is:", "source": "NCCN STS v2.2026", "correct": "Core needle biopsy (image-guided)", "choices": ["Core needle biopsy (image-guided)", "Excisional biopsy", "Incisional biopsy via transverse incision", "Fine needle aspiration (FNA)"], "explanation": "For STS: Core needle biopsy is preferred for large (>3cm) masses — provides adequate tissue for histology and grade while not violating tissue planes. Excisional biopsy is acceptable only for masses <3cm. NEVER do excisional biopsy on large suspected STS (violates planes, contaminates compartment). Incisional biopsy via LONGITUDINAL (not transverse) incision is alternative if core not feasible."},
{"id": 31, "cat": "Skin & STS", "q": "The recommended treatment for a high-grade (G3) 8 cm deep soft tissue sarcoma of the thigh is:", "source": "NCCN STS v2.2026", "correct": "Wide excision + radiation therapy ± chemotherapy", "choices": ["Wide excision + radiation therapy ± chemotherapy", "Wide excision alone (radiation not needed for extremity STS)", "Amputation (definitive local control)", "Chemotherapy alone (neoadjuvant) without surgery"], "explanation": "High-grade STS >5cm = multimodal treatment: surgery + radiation ± chemotherapy. Radiation can be pre-op or post-op (pre-op preferred by many: smaller field, better oxygenation, allows pathologic response assessment). Amputation is reserved for unresectable cases. Chemo (doxorubicin + ifosfamide) is added for metastatic risk reduction in selected high-grade cases."},
{"id": 32, "cat": "Skin & STS", "q": "The most common retroperitoneal soft tissue sarcoma is:", "source": "NCCN STS v2.2026", "correct": "Liposarcoma (well-differentiated and dedifferentiated subtypes)", "choices": ["Liposarcoma (well-differentiated and dedifferentiated subtypes)", "Leiomyosarcoma", "Synovial sarcoma", "Rhabdomyosarcoma"], "explanation": "Retroperitoneal sarcoma distribution: Liposarcoma ~45-50% (most common) > Leiomyosarcoma ~20%. Liposarcoma often presents very large (15-20cm) due to late symptoms. En bloc resection with adjacent organs (kidney commonly removed). Pre-op radiation preferred for retroperitoneal STS. Synovial sarcoma is most common in young adults/extremities."},
{"id": 33, "cat": "Skin & STS", "q": "Desmoid tumor (aggressive fibromatosis) differs from most sarcomas in that:", "source": "NCCN STS v2.2026", "correct": "It has NO metastatic potential despite being locally aggressive", "choices": ["It has NO metastatic potential despite being locally aggressive", "It responds completely to radiation and chemotherapy without surgery", "It is always associated with FAP/Gardner syndrome", "It arises only in the mesentery"], "explanation": "Desmoid tumors = locally aggressive fibromatosis with NO metastatic potential. Associated with FAP/Gardner (mesenteric desmoids) and sporadic cases (abdominal wall post-trauma/surgery). Treatment: watch-and-wait if stable → Sulindac/Tamoxifen → imatinib → surgery as LAST resort (high local recurrence ~25-50%). Avoid surgery unless causing obstruction or life-threatening complications."},
{"id": 34, "cat": "Skin & STS", "q": "Which feature of a cutaneous squamous cell carcinoma (SCC) indicates high risk requiring wider margins and consideration of adjuvant radiation?", "source": "NCCN SCC v2.2026", "correct": "Perineural invasion", "choices": ["Perineural invasion", "Well-differentiated histology", "Diameter 0.8 cm on the forearm", "Superficial extension limited to dermis"], "explanation": "High-risk SCC features: diameter >2cm, invasion beyond dermis (Clark IV-V), poor differentiation, perineural/lymphovascular invasion, immunosuppressed patient, recurrent tumor, ear/lip location. Perineural invasion particularly increases recurrence risk and is an indication for adjuvant radiation. Well-differentiated, small, superficial SCCs have low recurrence risk."},
{"id": 35, "cat": "Skin & STS", "q": "A patient on immunosuppression after renal transplant has a new skin lesion consistent with Kaposi sarcoma. What is the FIRST management step?", "source": "NCCN SCC v2.2026", "correct": "Reduce/modify immunosuppression (switch to mTOR inhibitor if possible)", "choices": ["Reduce/modify immunosuppression (switch to mTOR inhibitor if possible)", "Immediate wide excision with 2cm margins", "Radiation therapy to all lesions", "Systemic chemotherapy with liposomal doxorubicin"], "explanation": "For transplant-associated Kaposi sarcoma (HHV-8 driven): first step = reduce immunosuppression. Switch to mTOR inhibitor (sirolimus/everolimus) which has anti-tumor activity. For localized disease: observation, radiation, or excision. For disseminated disease: liposomal doxorubicin or paclitaxel."},
{"id": 204, "cat": "Skin & STS", "q": "Merkel cell carcinoma (MCC) is an aggressive cutaneous neuroendocrine tumor most commonly found on sun-exposed skin in elderly immunosuppressed patients. What is associated with Merkel cell polyomavirus (MCPyV) and its prognosis?", "source": "Merkel Cell Carcinoma / NCCN", "correct": "MCPyV-positive MCC (80%) has better prognosis than virus-negative; sentinel lymph node biopsy required", "choices": ["MCPyV-positive MCC (80%) has better prognosis than virus-negative; sentinel lymph node biopsy required", "MCC is always benign; observation only", "Virus-negative MCC is curable with radiation alone", "MCPyV-positive MCC does not require SLNB"], "explanation": "MCC: MCPyV-positive (~80%) has better prognosis than UV-driven virus-negative disease. Treatment: wide local excision (1–2 cm margins), SLNB (high rate of occult nodal mets ~30%), adjuvant radiation to primary site ± nodal basin. Immunotherapy (pembrolizumab, avelumab) for advanced/metastatic disease. Recurrence rate ~40%; 5-year OS ~40–65% depending on stage. High rates in immunosuppressed patients (transplant, HIV)."},
{"id": 205, "cat": "Skin & STS", "q": "A retroperitoneal liposarcoma is found incidentally on CT. It is 18 cm, well-differentiated, and appears to abut but not invade adjacent structures. What is the treatment goal?", "source": "NCCN STS Guidelines", "correct": "R0 resection with en-bloc removal of adjacent organs if needed (retroperitoneal liposarcoma requires wide resection)", "choices": ["R0 resection with en-bloc removal of adjacent organs if needed (retroperitoneal liposarcoma requires wide resection)", "Neoadjuvant chemotherapy before resection is always required", "Radiation alone is curative for retroperitoneal liposarcoma", "Biopsy only; retroperitoneal sarcomas are unresectable"], "explanation": "Retroperitoneal STS (predominantly liposarcoma, leiomyosarcoma): surgery is the only potentially curative treatment. Goal is R0 resection with wide surgical margins, often requiring en-bloc removal of ipsilateral kidney, adrenal, colon segment, psoas muscle. Recurrence rates are high (50–70% for liposarcoma). Neoadjuvant therapy for borderline resectable disease. Radiation: post-operative for high-grade histology, positive margins."},
{"id": 206, "cat": "Skin & STS", "q": "Desmoid tumors (aggressive fibromatosis) are locally aggressive tumors that do not metastasize. Which hereditary condition predisposes to intra-abdominal desmoids, and what is the first-line management for sporadic desmoids?", "source": "NCCN Desmoid Tumor Guidelines", "correct": "FAP (familial adenomatous polyposis) — APC mutation; first-line for sporadic: active surveillance or NSAIDs/sulindac", "choices": ["FAP (familial adenomatous polyposis) — APC mutation; first-line for sporadic: active surveillance or NSAIDs/sulindac", "MEN1; first-line is imatinib", "Li-Fraumeni syndrome; radiation is first-line", "No hereditary association; immediate surgery for all desmoids"], "explanation": "Desmoid tumors: FAP patients have 850× increased risk (mesenteric/abdominal desmoids, Gardner syndrome). APC mutation drives beta-catenin pathway. Sporadic desmoids: first-line is active surveillance (up to 50% spontaneously regress or stabilize) or NSAIDs (sulindac, celecoxib). Surgery has high recurrence (50–90%); reserved for resectable, symptomatic, or life-threatening desmoids. Systemic therapy: sorafenib (approved), imatinib, chemotherapy for progressive disease."},
{"id": 207, "cat": "Skin & STS", "q": "A 55-year-old with a history of chronic lymphedema of the right arm (post-mastectomy) develops a purple-red skin nodule on the arm. What is the most likely diagnosis?", "source": "Soft Tissue Sarcoma / Lymphangiosarcoma", "correct": "Lymphangiosarcoma (Stewart-Treves syndrome)", "choices": ["Lymphangiosarcoma (Stewart-Treves syndrome)", "Kaposi sarcoma", "Melanoma metastasis", "Benign lymphangioma"], "explanation": "Stewart-Treves syndrome: lymphangiosarcoma arising in a chronically lymphedematous extremity, classically after mastectomy (post-mastectomy lymphedema). Presents as purple/red multicentric skin nodules. Highly aggressive, 5-year survival <5%. Treatment: amputation ± chemotherapy/radiation (very poor prognosis regardless). Any new skin lesion in a chronically lymphedematous extremity warrants urgent biopsy."},
{"id": 208, "cat": "Skin & STS", "q": "In the AJCC staging system for soft tissue sarcoma, grade is a critical component. What histologic feature most determines tumor grade in STS?", "source": "AJCC STS Staging / FNCLCC Grading", "correct": "Mitotic rate + tumor differentiation + necrosis (FNCLCC grading system)", "choices": ["Mitotic rate + tumor differentiation + necrosis (FNCLCC grading system)", "Tumor size alone", "Margin status", "Presence of lymph node metastasis"], "explanation": "FNCLCC (French Federation of Cancer Centers) grading: (1) Tumor differentiation (1–3 points), (2) Mitotic count per 10 HPF (1–3 points), (3) Tumor necrosis (0–2 points). Total score: Grade 1 (2–3), Grade 2 (4–5), Grade 3 (6–8). Grade is the strongest predictor of metastasis and survival in STS, more than size or location. Grade 3 STS has ~50% rate of distant metastasis (lung most common)."},
{"id": 36, "cat": "Thyroid", "q": "A pregnant patient in her first trimester has severe hyperthyroidism. Which drug is preferred for treatment?", "source": "DOH CPG 2021 / ATA 2025", "correct": "PTU (propylthiouracil) — preferred in 1st trimester", "choices": ["PTU (propylthiouracil) — preferred in 1st trimester", "Methimazole (MMI) — preferred at all stages of pregnancy", "Radioactive iodine (RAI) — safe with fetal shielding", "Beta-blocker alone (atenolol) — avoids antithyroid drugs in 1st trimester"], "explanation": "PTU is preferred in 1st trimester (methimazole is teratogenic — aplasia cutis, choanal atresia). Switch to MMI in 2nd/3rd trimester (PTU carries hepatotoxicity risk long-term). RAI is absolutely contraindicated in pregnancy. For thyroid storm: PTU is also preferred because it also blocks peripheral T4→T3 conversion."},
{"id": 37, "cat": "Thyroid", "q": "A patient presenting with fever 40°C, heart rate 145, atrial fibrillation, agitation, and vomiting scores 52 on the Burch-Wartofsky scale. This represents:", "source": "DOH CPG 2021 / ATA 2025", "correct": "Thyroid storm — treat aggressively", "choices": ["Thyroid storm — treat aggressively", "Impending thyroid storm — close monitoring, start PTU", "Unlikely thyroid storm — investigate other causes", "Subclinical thyrotoxicosis — outpatient antithyroid therapy"], "explanation": "Burch-Wartofsky score: ≥45 = thyroid storm (treat aggressively); 25-44 = impending storm (treat as storm); <25 = unlikely. This score of 52 = thyroid storm. Components scored: temperature, CNS effects (agitation/psychosis/coma), GI/hepatic dysfunction, heart rate, CHF, AF, and presence of a precipitating event."},
{"id": 38, "cat": "Thyroid", "q": "In treating thyroid storm, iodine (Lugol's solution) must be given AFTER PTU because:", "source": "DOH CPG 2021 / ATA 2025", "correct": "PTU must first block synthesis; iodine given first would be organified and worsen thyrotoxicosis", "choices": ["PTU must first block synthesis; iodine given first would be organified and worsen thyrotoxicosis", "Iodine causes anaphylaxis when given before antithyroid drugs", "PTU enhances iodine absorption, so timing is for pharmacokinetic reasons", "Iodine inhibits PTU activity if given simultaneously"], "explanation": "The Wolff-Chaikoff effect (iodine suppresses thyroid hormone release) is the mechanism. BUT iodine must be given at least 1 hour AFTER PTU — otherwise iodine is used as substrate for MORE hormone synthesis (organified), worsening the storm. Order: (1) PTU, (2) Steroids, (3) Iodine (1hr after PTU), (4) Beta-blocker, (5) Supportive."},
{"id": 39, "cat": "Thyroid", "q": "Riedel's thyroiditis is characterized by:", "source": "DOH CPG 2021 / ATA 2025", "correct": "Dense fibrous replacement of thyroid, 'iron-hard' gland, IgG4-related disease", "choices": ["Dense fibrous replacement of thyroid, 'iron-hard' gland, IgG4-related disease", "Painful tender thyroid with elevated ESR after viral illness", "Autoimmune TPO antibodies with lymphocytic infiltration", "Suppurative infection requiring incision and drainage"], "explanation": "Riedel's thyroiditis = IgG4-related disease with dense fibrosis replacing the thyroid and invading surrounding structures (trachea, esophagus, vessels). 'Iron hard' on palpation. May cause hypothyroidism, dysphagia, dysphonia. Associated with other fibrosing conditions (retroperitoneal fibrosis, sclerosing cholangitis). Treatment: corticosteroids + tamoxifen."},
{"id": 40, "cat": "Thyroid", "q": "Hashimoto's thyroiditis carries an increased risk of which malignancy?", "source": "DOH CPG 2021 / ATA 2025", "correct": "Primary thyroid lymphoma (MALT/diffuse large B-cell)", "choices": ["Primary thyroid lymphoma (MALT/diffuse large B-cell)", "Papillary thyroid carcinoma", "Medullary thyroid carcinoma", "Follicular thyroid carcinoma"], "explanation": "Hashimoto's thyroiditis (chronic lymphocytic thyroiditis) is associated with an increased risk of primary thyroid lymphoma — particularly MALT lymphoma or diffuse large B-cell lymphoma. Rapid thyroid enlargement in a known Hashimoto patient should raise concern for lymphoma (not just goiter). Note: Hashimoto is also associated with slightly increased PTC risk, but lymphoma is the classic exam answer."},
{"id": 161, "cat": "Thyroid", "q": "A 40-year-old woman undergoes total thyroidectomy. On postoperative day 1, she develops perioral numbness and tingling. Serum calcium is 6.8 mg/dL. What is the most appropriate initial treatment?", "source": "Endocrine Surgery / Hypoparathyroidism", "correct": "IV calcium gluconate infusion", "choices": ["IV calcium gluconate infusion", "Oral calcium carbonate alone", "Calcitriol only", "Observation — symptoms will resolve"], "explanation": "Symptomatic hypocalcemia (perioral/digital paresthesias, Chvostek's sign, Trousseau's sign, tetany) after thyroidectomy = hypoparathyroidism. Symptomatic or calcium <7.5 mg/dL: IV calcium gluconate (1–2 g over 10–20 min, then infusion). Mild/asymptomatic: oral calcium + calcitriol (1,25-OH vitamin D to enhance absorption). Permanent hypoparathyroidism occurs in ~1–3% of total thyroidectomies."},
{"id": 162, "cat": "Thyroid", "q": "Injury to the external branch of the superior laryngeal nerve (EBSLN) during thyroidectomy causes which specific vocal change?", "source": "Thyroid Surgery / Nerve Injury", "correct": "Loss of high-pitched phonation (cricothyroid muscle weakness)", "choices": ["Loss of high-pitched phonation (cricothyroid muscle weakness)", "Complete aphonia", "Hoarseness from vocal cord paralysis", "Bovine cough only"], "explanation": "The EBSLN innervates the cricothyroid muscle (tensor of vocal cord, adjusts pitch). Injury → inability to reach high notes, voice fatigue, reduced vocal power — particularly devastating for singers/public speakers. The recurrent laryngeal nerve (RLN) injury causes vocal cord paralysis and hoarseness. Both nerves must be identified during thyroidectomy."},
{"id": 163, "cat": "Thyroid", "q": "A 35-year-old woman has a thyroid FNA showing 'follicular neoplasm.' Per the Bethesda classification, this is category IV. What is the recommended next step?", "source": "Bethesda System for Reporting Thyroid Cytopathology", "correct": "Diagnostic thyroid lobectomy (20–30% risk of malignancy)", "choices": ["Diagnostic thyroid lobectomy (20–30% risk of malignancy)", "Total thyroidectomy immediately", "Repeat FNA in 3 months", "Observation with serial ultrasound"], "explanation": "Bethesda IV (Follicular Neoplasm/Suspicious for FN): cytology cannot distinguish follicular adenoma from follicular carcinoma (capsular/vascular invasion determines malignancy on histology). Malignancy risk 25–40%. Diagnostic lobectomy allows histologic diagnosis; if malignant, completion thyroidectomy follows. Total thyroidectomy upfront is acceptable if large bilateral disease or patient preference."},
{"id": 164, "cat": "Thyroid", "q": "Medullary thyroid carcinoma (MTC) arises from parafollicular C cells and secretes calcitonin. In which clinical syndrome does MTC occur in 100% of affected patients if untreated?", "source": "ATA MTC Guidelines", "correct": "MEN2A and MEN2B (RET proto-oncogene mutations)", "choices": ["MEN2A and MEN2B (RET proto-oncogene mutations)", "MEN1", "Familial adenomatous polyposis", "Cowden syndrome"], "explanation": "MTC occurs in: MEN2A (MTC, pheochromocytoma, parathyroid hyperplasia — RET codon 634), MEN2B (MTC, pheo, mucosal neuromas, marfanoid habitus — RET codon 918), and Familial MTC. RET codon 918 (MEN2B) → most aggressive MTC, prophylactic thyroidectomy by age 6 months. Calcitonin is the tumor marker; CEA useful for disease monitoring. All MTC: test for RET mutation."},
{"id": 165, "cat": "Thyroid", "q": "A 65-year-old woman has a rapidly enlarging thyroid mass with vocal cord paralysis and hoarseness. FNA shows undifferentiated pleomorphic cells. What is the prognosis and management?", "source": "ATA Thyroid Cancer Guidelines", "correct": "Anaplastic thyroid carcinoma (ATC); median survival 3–5 months; multimodal therapy (surgery if resectable + chemoradiation)", "choices": ["Anaplastic thyroid carcinoma (ATC); median survival 3–5 months; multimodal therapy (surgery if resectable + chemoradiation)", "Poorly differentiated thyroid cancer; radioactive iodine curative", "Thyroid lymphoma; chemotherapy curative", "Medullary thyroid cancer; total thyroidectomy curative"], "explanation": "ATC is AJCC stage IV by definition and carries median survival of 3–5 months (<20% 1-year survival). ~50% have distant metastases at diagnosis. Management: if resectable → R0 resection + adjuvant chemoradiation (doxorubicin-based). BRAF V600E mutation in ~45% → dabrafenib+trametinib shows promising response. Tracheostomy for airway control. Thyroid lymphoma (MALT): chemotherapy/radiation, much better prognosis."},
{"id": 166, "cat": "Thyroid", "q": "A 30-year-old man undergoes total thyroidectomy for papillary thyroid cancer (PTC). Final pathology shows a 1.2 cm PTC (T1b) without lymph node metastases (N0) in a single lobe. What is the preferred adjuvant treatment?", "source": "ATA Thyroid Cancer Guidelines 2015", "correct": "Thyroid hormone suppression (TSH suppression); RAI not routinely indicated for low-risk T1b N0", "choices": ["Thyroid hormone suppression (TSH suppression); RAI not routinely indicated for low-risk T1b N0", "Radioactive iodine (RAI) I-131 ablation is mandatory", "External beam radiation", "No further treatment needed"], "explanation": "ATA risk stratification for PTC: low-risk (T1-2, N0, no vascular invasion) → thyroid hormone suppression to keep TSH below normal (0.1–0.5 mIU/L). RAI is NOT routinely recommended for low-risk PTC ≤4 cm, N0. RAI indications: high-risk features (T4, N1b, M1, extrathyroidal extension, vascular invasion). Over-treatment with RAI causes unnecessary risks (salivary gland injury, leukemia)."},
{"id": 167, "cat": "Thyroid", "q": "Hurthle cell carcinoma (oncocytic carcinoma) of the thyroid is distinct from follicular carcinoma in which important clinical behavior?", "source": "ATA Thyroid Guidelines / Hurthle Cell", "correct": "Less RAI-avid than follicular carcinoma (poorer response to radioactive iodine)", "choices": ["Less RAI-avid than follicular carcinoma (poorer response to radioactive iodine)", "Always benign; no malignant potential", "More RAI-avid than papillary carcinoma", "Does not metastasize to lymph nodes"], "explanation": "Hurthle cell (oncocytic) carcinoma: subtype of follicular-derived carcinoma. Key distinction: Hurthle cell tumors are typically RAI-non-avid (due to loss of NIS expression) — unlike follicular carcinoma which may respond to RAI. Hurthle cells have abundant mitochondria-rich eosinophilic cytoplasm. Diagnosis requires capsular/vascular invasion. Metastasizes hematogenously (bone, lung) and to lymph nodes more than follicular Ca."},
{"id": 168, "cat": "Thyroid", "q": "Thyroid storm (thyrotoxic crisis) can be precipitated by surgery in an unprepared hyperthyroid patient. Which component of treatment specifically blocks the peripheral conversion of T4 to the active T3?", "source": "Endocrinology / Thyroid Storm", "correct": "Propylthiouracil (PTU) — and high-dose glucocorticoids", "choices": ["Propylthiouracil (PTU) — and high-dose glucocorticoids", "Methimazole", "Potassium iodide (Lugol's solution)", "Beta blockers (propranolol)"], "explanation": "Thyroid storm treatment (Burch-Wartofsky): (1) PTU 500–1000 mg load → blocks synthesis AND T4→T3 conversion; (2) Glucocorticoids (hydrocortisone) → also block T4→T3; (3) Iodine (Lugol's/SSKI) given 1h AFTER PTU → inhibits hormone release (Wolff-Chaikoff); (4) Beta-blockers (propranolol IV) → control heart rate and inhibit some T4→T3; (5) Treat precipitating cause. Methimazole does NOT block peripheral conversion."},
{"id": 169, "cat": "Thyroid", "q": "'Lateral aberrant thyroid' (thyroid tissue in lateral neck lymph nodes) in an adult is best interpreted as:", "source": "Thyroid Surgery / Pathology", "correct": "Metastatic papillary thyroid carcinoma until proven otherwise", "choices": ["Metastatic papillary thyroid carcinoma until proven otherwise", "Benign ectopic thyroid tissue — observe", "Normal anatomical variant", "Thyroglossal duct remnant"], "explanation": "True ectopic lateral thyroid tissue is exceedingly rare after birth (most reported cases were actually misidentified PTC nodal mets). Any thyroid tissue in an adult lateral neck lymph node should be presumed PTC nodal metastasis until proven otherwise — biopsy will show PTC features (papillary architecture, nuclear grooves, psammoma bodies). Thyroglossal duct remnants are midline."},
{"id": 170, "cat": "Thyroid", "q": "A patient with Graves' disease is preparing for thyroidectomy. Lugol's iodine solution is given 10 days preoperatively to achieve which goal?", "source": "Thyroid Surgery Preoperative Management", "correct": "Reduce thyroid vascularity and firmness (decrease intraoperative bleeding)", "choices": ["Reduce thyroid vascularity and firmness (decrease intraoperative bleeding)", "Permanently reduce thyroid hormone synthesis", "Induce hypothyroidism before surgery", "Replace antithyroid drugs"], "explanation": "Lugol's iodine (KI) given 10–14 days preoperatively in Graves' disease: invokes Wolff-Chaikoff effect and reduces thyroid blood flow and vascularity (thyroid becomes firmer, less vascular) — making surgery safer with less bleeding. It does NOT permanently inhibit hormone synthesis (escape phenomenon occurs after ~10 days). Antithyroid drugs (methimazole/PTU) + beta blockers ensure euthyroid state first."},
{"id": 86, "cat": "Adrenal", "q": "A 38-year-old presents with hypertensive crises, diaphoresis, and headaches. 24-hour urine shows elevated metanephrines. Which medication must be started FIRST before any surgical intervention?", "source": "Endocrine Surgery guidelines / AHA", "correct": "Alpha-adrenergic blockade (phenoxybenzamine)", "choices": ["Alpha-adrenergic blockade (phenoxybenzamine)", "Beta-adrenergic blockade (propranolol)", "Metyrosine (alpha-methyl-tyrosine)", "IV fluid resuscitation alone"], "explanation": "For pheochromocytoma, alpha blockade MUST precede beta blockade. Starting beta blockers first with an unblocked alpha receptor causes unopposed vasoconstriction and hypertensive crisis. Phenoxybenzamine (non-selective irreversible alpha blocker) is initiated 1–2 weeks preop, then beta blockade added if needed for tachycardia."},
{"id": 87, "cat": "Adrenal", "q": "When prepping a pheochromocytoma patient for surgery, beta blockers are added after alpha blockade primarily to control:", "source": "Endocrine Surgery guidelines", "correct": "Reflex tachycardia from alpha blockade", "choices": ["Reflex tachycardia from alpha blockade", "Hypertensive crises", "Catecholamine synthesis", "Cortisol excess"], "explanation": "Alpha blockade causes vasodilation, which triggers reflex tachycardia. Beta blockers are added only AFTER adequate alpha blockade to control this tachycardia. Adding beta blockers first causes unopposed alpha stimulation → severe hypertension."},
{"id": 88, "cat": "Adrenal", "q": "A 45-year-old has hypertension, hypokalemia, and suppressed renin with elevated aldosterone. CT shows a 1.8 cm right adrenal adenoma. What is the next best step to confirm unilateral disease before adrenalectomy?", "source": "Endocrine Society Guidelines / Primary Hyperaldosteronism", "correct": "Adrenal vein sampling (AVS)", "choices": ["Adrenal vein sampling (AVS)", "Proceed directly to right adrenalectomy", "Dexamethasone suppression test", "Repeat CT in 6 months"], "explanation": "In primary hyperaldosteronism, adrenal vein sampling (AVS) is the gold standard to confirm lateralization before surgery. CT alone misidentifies the side in ~25% of cases (bilateral disease, contralateral incidentaloma). AVS is recommended for all patients who are surgical candidates when CT is not clearly unilateral bilateral disease."},
{"id": 89, "cat": "Adrenal", "q": "The 'rule of 10s' for pheochromocytoma states that approximately 10% are bilateral, 10% are extra-adrenal, 10% are malignant, and 10% occur in children. Extra-adrenal pheochromocytomas (paragangliomas) are most commonly located in the:", "source": "Surgical Oncology / Endocrine Surgery", "correct": "Organ of Zuckerkandl (para-aortic at IMA origin)", "choices": ["Organ of Zuckerkandl (para-aortic at IMA origin)", "Bladder wall", "Mediastinum", "Carotid body"], "explanation": "The organ of Zuckerkandl, located near the origin of the inferior mesenteric artery along the aorta, is the most common site for extra-adrenal pheochromocytoma. Bladder paragangliomas cause hypertension with micturition. All these are chromaffin tissue remnants of the sympathetic chain."},
{"id": 90, "cat": "Adrenal", "q": "A 32-year-old with MEN2A presents for prophylactic thyroidectomy. Preoperative workup reveals elevated 24-hour urinary catecholamines. What is the correct sequence of surgical management?", "source": "ATA MEN2 Guidelines", "correct": "Adrenalectomy first, then thyroidectomy", "choices": ["Adrenalectomy first, then thyroidectomy", "Thyroidectomy first, then adrenalectomy", "Bilateral adrenalectomy and thyroidectomy simultaneously", "Thyroidectomy only; observe adrenal"], "explanation": "In MEN2A with concurrent pheochromocytoma and medullary thyroid cancer, the pheochromocytoma MUST be resected first. Anesthetic induction for thyroidectomy without prior pheochromocytoma resection risks catecholamine crisis. After adrenalectomy and recovery, thyroidectomy proceeds safely."},
{"id": 91, "cat": "Adrenal", "q": "A 55-year-old woman with a history of Cushing's disease undergoes transsphenoidal resection of a pituitary adenoma. Six months later she develops enlarging bitemporal visual field defects and hyperpigmentation. What is the diagnosis?", "source": "Endocrinology / Nelson's Syndrome", "correct": "Nelson's syndrome (post-adrenalectomy pituitary tumor expansion)", "choices": ["Nelson's syndrome (post-adrenalectomy pituitary tumor expansion)", "Recurrent Cushing's disease", "Secondary adrenal insufficiency", "Empty sella syndrome"], "explanation": "Nelson's syndrome occurs after bilateral adrenalectomy for Cushing's disease: loss of cortisol feedback causes the pre-existing ACTH-secreting pituitary adenoma to grow aggressively. Hallmarks: hyperpigmentation (from high ACTH/MSH), visual field defects from chiasm compression, and very high ACTH levels."},
{"id": 92, "cat": "Adrenal", "q": "A patient presents in adrenal crisis with hypotension, hypoglycemia, and hyponatremia. Which is the most appropriate immediate treatment?", "source": "Endocrine Emergency Management", "correct": "IV hydrocortisone 100 mg bolus + IV normal saline", "choices": ["IV hydrocortisone 100 mg bolus + IV normal saline", "Oral fludrocortisone + oral rehydration", "IM dexamethasone only", "IV dextrose only"], "explanation": "Adrenal crisis is life-threatening. Treatment: IV hydrocortisone 100 mg bolus (then 50–100 mg q6–8h) plus aggressive IV saline resuscitation (1L NS rapidly). Hydrocortisone at stress doses also provides adequate mineralocorticoid activity. Dexamethasone has no mineralocorticoid effect and may worsen hyponatremia."},
{"id": 93, "cat": "Adrenal", "q": "A 2 cm adrenal incidentaloma is found on CT done for abdominal pain. What is the minimal biochemical workup required for ALL adrenal incidentalomas regardless of imaging characteristics?", "source": "Endocrine Society Guidelines 2016", "correct": "1 mg overnight dexamethasone suppression test + plasma metanephrines + aldosterone/renin ratio (if hypertensive)", "choices": ["1 mg overnight dexamethasone suppression test + plasma metanephrines + aldosterone/renin ratio (if hypertensive)", "CT-guided biopsy", "Repeat CT in 3 months only", "24-hour urine cortisol only"], "explanation": "All adrenal incidentalomas require biochemical exclusion of: (1) subclinical Cushing's — 1 mg overnight DST; (2) pheochromocytoma — plasma/urine metanephrines; (3) primary hyperaldosteronism if hypertensive — ARR. CT biopsy is contraindicated unless pheochromocytoma is excluded (risk of hypertensive crisis)."},
{"id": 94, "cat": "Adrenal", "q": "An adrenocortical carcinoma (ACC) is resected. Pathology shows a Weiss score of 4. Which single feature of the Weiss criteria carries the greatest prognostic weight for malignancy?", "source": "Surgical Pathology / ACC", "correct": "Venous invasion", "choices": ["Venous invasion", "Mitotic rate >5/50 HPF", "Necrosis", "Capsular invasion"], "explanation": "The Weiss scoring system uses 9 criteria for ACC; a score ≥3 is malignant. Among these, vascular (venous) invasion, atypical mitoses, and diffuse architecture carry the most significant prognostic weight. Venous invasion specifically correlates with distant metastasis and poor survival."},
{"id": 95, "cat": "Adrenal", "q": "In Cushing's syndrome, which test best distinguishes a pituitary source (Cushing's disease) from an ectopic ACTH source?", "source": "Endocrinology Cushing's workup", "correct": "High-dose dexamethasone suppression test (8 mg overnight)", "choices": ["High-dose dexamethasone suppression test (8 mg overnight)", "Low-dose dexamethasone suppression test (1 mg)", "Midnight salivary cortisol", "24-hour urine free cortisol"], "explanation": "In Cushing's disease (pituitary adenoma), cortisol suppresses by >50% with high-dose (8 mg) dexamethasone due to partial feedback sensitivity. Ectopic ACTH sources (small cell lung, carcinoid) and adrenal tumors do NOT suppress. The inferior petrosal sinus sampling (IPSS) is the gold standard for localization."},
{"id": 96, "cat": "Adrenal", "q": "A patient has a 6 cm adrenal mass with CT Hounsfield units of 35 (unenhanced) and 20% contrast washout at 15 minutes. These findings are most consistent with:", "source": "ACR / Adrenal Imaging Guidelines", "correct": "Adrenocortical carcinoma (indeterminate/malignant features)", "choices": ["Adrenocortical carcinoma (indeterminate/malignant features)", "Adrenal adenoma (lipid-rich)", "Pheochromocytoma", "Myelolipoma"], "explanation": "Adrenal adenomas are lipid-rich (HU ≤10 unenhanced) or show >60% absolute washout at 15 min. HU of 35 with poor washout (<60% absolute, <40% relative) is indeterminate/suspicious. Size >4 cm also raises malignancy concern. Myelolipoma has HU <−20 (macroscopic fat). This pattern warrants adrenalectomy."},
{"id": 97, "cat": "Adrenal", "q": "Which adrenal condition requires cortisol replacement immediately after ipsilateral adrenalectomy even when the contralateral adrenal appears normal?", "source": "Endocrine Surgery", "correct": "Subclinical Cushing's syndrome (autonomous cortisol secretion)", "choices": ["Subclinical Cushing's syndrome (autonomous cortisol secretion)", "Primary hyperaldosteronism", "Non-functioning adenoma", "Pheochromocytoma"], "explanation": "In subclinical Cushing's, the adenoma chronically suppresses the contralateral adrenal via feedback. After resection, the contralateral adrenal may take weeks to months to recover. Perioperative hydrocortisone replacement is essential to prevent adrenal insufficiency. Primary hyperaldosteronism and pheochromocytoma do not suppress glucocorticoid axis."},
{"id": 98, "cat": "Adrenal", "q": "A laparoscopic adrenalectomy is planned. Which feature is an absolute indication for OPEN adrenalectomy instead?", "source": "SAGES / Adrenal Surgery Guidelines", "correct": "Radiographic evidence of local invasion or IVC involvement", "choices": ["Radiographic evidence of local invasion or IVC involvement", "Tumor size 5–6 cm", "Prior ipsilateral abdominal surgery", "Pheochromocytoma"], "explanation": "Absolute indications for open adrenalectomy include: suspected ACC with local invasion, IVC/renal vein involvement, or en-bloc resection needed. Large size alone (>6 cm) is a relative indication but not absolute. Pheochromocytoma can be done laparoscopically safely after proper alpha blockade. Prior surgery is a relative contraindication."},
{"id": 99, "cat": "Adrenal", "q": "Primary hyperaldosteronism (Conn's syndrome) classically presents with hypertension and hypokalemia. However, what percentage of patients have NORMAL serum potassium at presentation?", "source": "Endocrine Society / Primary Hyperaldosteronism", "correct": "~50% (hypokalemia is absent in many cases)", "choices": ["~50% (hypokalemia is absent in many cases)", "~5% (hypokalemia is almost universal)", "~90% (nearly all patients are normokalemic)", "100% (Conn's never causes hypokalemia)"], "explanation": "Historically Conn's was defined by hypokalemia, but contemporary series show ~50% of patients with primary hyperaldosteronism are normokalemic. Screening with the aldosterone-to-renin ratio (ARR) should be done for all patients with resistant hypertension, regardless of potassium level."},
{"id": 100, "cat": "Adrenal", "q": "A pregnant woman at 16 weeks gestation is found to have a pheochromocytoma. Which is the preferred surgical approach?", "source": "Endocrine Surgery / Pregnancy", "correct": "Laparoscopic adrenalectomy in the second trimester after alpha blockade", "choices": ["Laparoscopic adrenalectomy in the second trimester after alpha blockade", "Delay surgery until after delivery", "Open adrenalectomy in the first trimester", "Medical management only throughout pregnancy"], "explanation": "Pheochromocytoma in pregnancy has very high maternal and fetal mortality if untreated (~50%). The preferred approach is laparoscopic adrenalectomy in the second trimester (14–24 weeks) after adequate alpha blockade. First trimester risks organogenesis; third trimester risks premature labor. Medical management alone is not definitive."},
{"id": 101, "cat": "Spleen", "q": "A 25-year-old undergoes splenectomy for trauma. Which encapsulated organisms pose the greatest risk for overwhelming post-splenectomy infection (OPSI)?", "source": "ATLS / Immunology post-splenectomy", "correct": "Streptococcus pneumoniae, Haemophilus influenzae, Neisseria meningitidis", "choices": ["Streptococcus pneumoniae, Haemophilus influenzae, Neisseria meningitidis", "Staphylococcus aureus, E. coli, Klebsiella", "Pseudomonas, Enterococcus, Candida", "Listeria, Salmonella, Bartonella"], "explanation": "OPSI is most commonly caused by encapsulated organisms: S. pneumoniae (~50–90%), H. influenzae, and N. meningitidis. The spleen is critical for clearing encapsulated bacteria via opsonization (IgM, properdin, tuftsin). Mortality of OPSI is 50–70%. Vaccination + prophylactic penicillin are essential."},
{"id": 102, "cat": "Spleen", "q": "When should post-splenectomy vaccinations (pneumococcal, meningococcal, Hib) ideally be administered in an elective splenectomy?", "source": "ACIP / CDC Vaccination Guidelines", "correct": "At least 2 weeks BEFORE elective splenectomy", "choices": ["At least 2 weeks BEFORE elective splenectomy", "Immediately after splenectomy in the recovery room", "6 weeks after splenectomy", "Only if the patient develops infection"], "explanation": "For elective splenectomy, vaccines should be given ≥2 weeks preoperatively when the immune system is intact for optimal response. For emergency splenectomy, vaccines are given 2 weeks postoperatively (when immune function has partially recovered). Revaccination schedules apply for pneumococcal vaccines."},
{"id": 103, "cat": "Spleen", "q": "A 28-year-old woman with ITP has a platelet count of 8,000 and failed 6 weeks of corticosteroids. What is the recommended next step?", "source": "ASH ITP Guidelines 2019", "correct": "Rituximab or thrombopoietin receptor agonists (TPO-RAs) as second-line; splenectomy if refractory", "choices": ["Rituximab or thrombopoietin receptor agonists (TPO-RAs) as second-line; splenectomy if refractory", "Immediate splenectomy", "Platelet transfusion and discharge", "Bone marrow biopsy before any treatment"], "explanation": "Current ITP management: corticosteroids first-line; if failed, second-line options include rituximab, TPO-RAs (eltrombopag, romiplostim), or splenectomy. Splenectomy achieves durable remission in ~60–70% but is now reserved for patients failing multiple medical therapies due to surgical risk and advent of effective biologics."},
{"id": 104, "cat": "Spleen", "q": "In hereditary spherocytosis, what is the primary mechanism causing hemolytic anemia and splenomegaly?", "source": "Hematology / Hereditary Spherocytosis", "correct": "Defective spectrin/ankyrin in RBC membrane → spherocytes trapped and destroyed in splenic cords", "choices": ["Defective spectrin/ankyrin in RBC membrane → spherocytes trapped and destroyed in splenic cords", "G6PD deficiency causing oxidative hemolysis", "Autoimmune IgG coating of RBCs", "Abnormal hemoglobin polymerization"], "explanation": "Hereditary spherocytosis results from mutations in spectrin, ankyrin, band 3, or protein 4.2 → RBCs lose their biconcave shape → spherocytes with reduced deformability → trapped in splenic sinusoids → extravascular hemolysis. Splenectomy is curative for the anemia and prevents pigment gallstones but does not fix the underlying membrane defect."},
{"id": 105, "cat": "Spleen", "q": "Which splenic artery aneurysm (SAA) feature is an absolute indication for intervention regardless of size?", "source": "SVS Guidelines / Splenic Artery Aneurysm", "correct": "Pregnancy or planned pregnancy", "choices": ["Pregnancy or planned pregnancy", "Size >2 cm in a non-pregnant patient", "Incidental discovery in a 70-year-old", "Calcified wall (eggshell calcification)"], "explanation": "Absolute indications for SAA treatment: (1) pregnancy or women of childbearing age planning pregnancy (rupture risk approaches 95% in pregnancy with 70% maternal and 90% fetal mortality), (2) symptomatic aneurysms, (3) pseudoaneurysms (always repair), (4) size >2 cm is a relative indication. Eggshell calcification is NOT protective; it does NOT prevent rupture."},
{"id": 106, "cat": "Spleen", "q": "A 30-year-old with sickle cell disease presents with acute left upper quadrant pain and hypotension. Ultrasound shows massive splenomegaly (spleen weight estimated 1,200 g). What is the most likely diagnosis?", "source": "Hematology / Sickle Cell Disease", "correct": "Acute splenic sequestration crisis", "choices": ["Acute splenic sequestration crisis", "Splenic infarction", "Spontaneous splenic rupture", "Splenic abscess"], "explanation": "Acute splenic sequestration crisis occurs predominantly in young children with sickle cell disease (adults usually have autosplenectomy by repeated infarcts, but can occur in HbSC disease). Massive pooling of RBCs in the spleen causes sudden splenomegaly, severe anemia (Hgb drop >2g/dL), and hypovolemia. Tx: RBC transfusion; recurrent cases → splenectomy."},
{"id": 107, "cat": "Spleen", "q": "An accessory spleen is found during laparoscopic cholecystectomy. Where is the most common location for an accessory spleen?", "source": "Surgical Anatomy", "correct": "Splenic hilum", "choices": ["Splenic hilum", "Greater omentum", "Mesocolon", "Retroperitoneum"], "explanation": "Accessory spleens (splenunculi) are present in ~10–30% of people. The most common location is the splenic hilum (~75%), followed by the gastrosplenic ligament, greater omentum, and tail of the pancreas. Clinically important in ITP or hereditary spherocytosis — missed accessory spleen causes disease recurrence after splenectomy."},
{"id": 108, "cat": "Spleen", "q": "A patient with portal hypertension and cirrhosis develops thrombocytopenia (<50,000), leukopenia, and anemia. The most appropriate surgical treatment for symptomatic hypersplenism is:", "source": "Hepatology / Hypersplenism", "correct": "Splenectomy (or partial splenic embolization as alternative)", "choices": ["Splenectomy (or partial splenic embolization as alternative)", "TIPS placement", "Liver transplant listing only", "Observation; hypersplenism is never treated surgically"], "explanation": "Hypersplenism from portal hypertension causes pancytopenia due to splenic sequestration. Splenectomy is effective but risky in cirrhosis (bleeding, hepatic decompensation). Partial splenic embolization (PSE) is an alternative with lower morbidity. TIPS improves portal hypertension but inconsistently resolves hypersplenism. Ultimately liver transplant addresses the underlying cause."},
{"id": 109, "cat": "Spleen", "q": "A trauma patient sustains a grade III splenic laceration on CT. Hemodynamically, their BP is 105/70, HR 95, and they respond to 1L IV fluid resuscitation. What is the most appropriate initial management?", "source": "EAST / AAST Splenic Injury Guidelines", "correct": "Non-operative management (NOM) with admission, serial exams, and repeat CT at 24–48 hours", "choices": ["Non-operative management (NOM) with admission, serial exams, and repeat CT at 24–48 hours", "Immediate exploratory laparotomy", "Angioembolization immediately", "Laparoscopic splenorrhaphy"], "explanation": "NOM is successful in >85% of hemodynamically stable blunt splenic injuries (grades I–IV). Criteria for NOM: hemodynamic stability, no peritoneal signs, no other operative injuries. Angioembolization is added for grade III–V with blush on CT or failure of NOM. Operative management for hemodynamic instability or NOM failure."},
{"id": 110, "cat": "Spleen", "q": "Delayed splenic rupture is defined as hemorrhage occurring how many days after initial trauma in a patient who appeared stable?", "source": "Trauma Surgery / Delayed Splenic Rupture", "correct": "≥48 hours (classically described as up to 2 weeks) after injury", "choices": ["≥48 hours (classically described as up to 2 weeks) after injury", "Within 6 hours of injury", ">1 month after injury", "Only in patients on anticoagulation"], "explanation": "Delayed splenic rupture is defined as hemorrhage ≥48 hours after trauma in a patient who was initially hemodynamically stable. It results from expansion of a subcapsular hematoma that eventually ruptures. Incidence ~1%. Risk factors: large subcapsular hematoma (>50% of splenic surface) on initial CT, grade III–IV injuries."},
{"id": 111, "cat": "Spleen", "q": "Splenic vein thrombosis causing left-sided (sinistral) portal hypertension most commonly results in which unique complication?", "source": "HPB Surgery / Splenic Vein Thrombosis", "correct": "Gastric varices without esophageal varices", "choices": ["Gastric varices without esophageal varices", "Esophageal varices with normal liver function", "Hepatic encephalopathy", "Ascites"], "explanation": "Splenic vein thrombosis (most common cause: chronic pancreatitis) causes isolated left-sided (sinistral) portal hypertension. Blood flows retrograde via short gastric veins → gastric fundal varices, while portal pressure is normal (no esophageal varices). Splenectomy is curative (eliminates the source of increased blood flow through collaterals)."},
{"id": 112, "cat": "Spleen", "q": "In warm autoimmune hemolytic anemia (wAIHA), RBCs are coated with IgG antibodies. What is the initial treatment and why does splenectomy work as second-line therapy?", "source": "Hematology / AIHA", "correct": "Steroids first-line; splenectomy removes the site of IgG-coated RBC destruction", "choices": ["Steroids first-line; splenectomy removes the site of IgG-coated RBC destruction", "Plasmapheresis first-line; splenectomy removes antibody production", "IVIG first-line; splenectomy removes complement", "Splenectomy is always first-line for wAIHA"], "explanation": "wAIHA: IgG-coated RBCs are recognized by Fc receptors on splenic macrophages → extravascular hemolysis. Steroids (first-line) reduce antibody production and splenic destruction. Splenectomy (second-line) removes the primary site of hemolysis and a major site of antibody production → response rate ~60–70%."},
{"id": 113, "cat": "Spleen", "q": "Hairy cell leukemia (HCL) is associated with massive splenomegaly. What is the current first-line treatment for HCL, and when is splenectomy indicated?", "source": "Hematology / HCL", "correct": "Cladribine (2-CdA) first-line; splenectomy for refractory disease or urgent cytopenia", "choices": ["Cladribine (2-CdA) first-line; splenectomy for refractory disease or urgent cytopenia", "Splenectomy is always first-line for HCL", "Rituximab first-line; splenectomy never indicated", "Observation only; HCL is indolent"], "explanation": "HCL: cladribine (purine nucleoside analogue) achieves complete remission in ~80–90% and is the current first-line treatment. Splenectomy was the historical treatment before cladribine but is now reserved for: massive symptomatic splenomegaly, cytopenias requiring rapid correction, or refractory disease."},
{"id": 114, "cat": "Spleen", "q": "During splenectomy, which ligament must be carefully divided to avoid injury to the tail of the pancreas?", "source": "Surgical Anatomy / Splenectomy", "correct": "Splenorenal (lienorenal) ligament", "choices": ["Splenorenal (lienorenal) ligament", "Gastrosplenic ligament", "Splenophrenic ligament", "Splenocolic ligament"], "explanation": "The tail of the pancreas lies within 1 cm of the splenic hilum in ~75% of patients and actually touches the splenic hilum in ~30%. When dividing the splenorenal (lienorenal) ligament — which contains the splenic vessels and is in close proximity to the pancreatic tail — care must be taken to avoid pancreatic injury, which can cause a postoperative pancreatic fistula."},
{"id": 115, "cat": "Spleen", "q": "A patient with Gaucher disease type 1 has progressive splenomegaly causing abdominal pain and early satiety. What is the preferred treatment that has largely replaced splenectomy?", "source": "Gaucher Disease / NGNP Guidelines", "correct": "Enzyme replacement therapy (imiglucerase/velaglucerase)", "choices": ["Enzyme replacement therapy (imiglucerase/velaglucerase)", "Splenectomy remains the treatment of choice", "Bone marrow transplantation", "Substrate reduction therapy (miglustat)"], "explanation": "Gaucher disease type 1 (non-neuronopathic) results from glucocerebrosidase deficiency → glucocerebroside accumulates in macrophages → splenomegaly, hepatomegaly, and bone disease. Enzyme replacement therapy (ERT) is first-line and has dramatically reduced the need for splenectomy. Splenectomy may worsen bone disease and is now rarely performed."},
{"id": 116, "cat": "Liver", "q": "Which criteria must be met for a cirrhotic patient with hepatocellular carcinoma (HCC) to be listed for liver transplantation under the Milan criteria?", "source": "Milan Criteria / UNOS", "correct": "Single tumor ≤5 cm OR up to 3 tumors each ≤3 cm, no vascular invasion, no extrahepatic disease", "choices": ["Single tumor ≤5 cm OR up to 3 tumors each ≤3 cm, no vascular invasion, no extrahepatic disease", "Any HCC in cirrhosis regardless of size", "Single tumor ≤8 cm with AFP <400", "Up to 5 tumors each ≤5 cm (UCSF criteria)"], "explanation": "Milan criteria for liver transplantation in HCC: solitary tumor ≤5 cm OR ≤3 nodules each ≤3 cm, without macrovascular invasion or extrahepatic spread. Patients meeting Milan criteria have 5-year survival ~70% post-transplant. UCSF criteria are expanded (solitary ≤6.5 cm or ≤3 nodules ≤4.5 cm each, total ≤8 cm)."},
{"id": 117, "cat": "Liver", "q": "A 35-year-old woman on oral contraceptive pills has a 4 cm liver lesion found incidentally. MRI shows central scar with spoke-wheel enhancement pattern. What is the most likely diagnosis and management?", "source": "Hepatic Benign Tumors / HPB Surgery", "correct": "Focal nodular hyperplasia (FNH); observation, no surgery needed", "choices": ["Focal nodular hyperplasia (FNH); observation, no surgery needed", "Hepatic adenoma; stop OCPs and consider resection", "Hemangioma; observation", "Hepatocellular carcinoma; resect"], "explanation": "FNH has a central fibrous scar with radiating septa (spoke-wheel on MRI with Tc-99m sulfur colloid scan showing uptake). It is a benign hamartomatous lesion with no malignant potential and minimal rupture risk. Management: observation. Contrast it with hepatic adenoma (no central scar, risk of rupture/malignancy, associated with OCPs → stop OCPs, consider resection if >5 cm)."},
{"id": 118, "cat": "Liver", "q": "A 32-year-old woman on OCP has a 6 cm hepatic adenoma. She stops OCPs. After 6 months it remains 6 cm. What is the next management step?", "source": "HPB Surgery / Hepatic Adenoma", "correct": "Surgical resection (risk of rupture and malignant transformation for adenomas >5 cm)", "choices": ["Surgical resection (risk of rupture and malignant transformation for adenomas >5 cm)", "Continue observation; no intervention needed", "Liver transplantation", "Arterial embolization only"], "explanation": "Hepatic adenomas >5 cm carry significant risk: rupture (up to 20–25%), hemorrhage, and malignant transformation (~4–8%). Resection is recommended for adenomas >5 cm that persist after OCP cessation, all men (higher malignancy risk), and symptomatic adenomas. Adenomas <5 cm with OCP cessation may regress; observe with serial MRI."},
{"id": 119, "cat": "Liver", "q": "What is the Couinaud segment that receives blood supply from the left and right portal branches and is therefore used as the boundary for major hepatic resections?", "source": "Surgical Anatomy / Couinaud Segments", "correct": "Segment IV (quadrate lobe) — divides right and left livers at the Rex-Cantlie line", "choices": ["Segment IV (quadrate lobe) — divides right and left livers at the Rex-Cantlie line", "Segment I (caudate lobe)", "Segment VII", "Segment V"], "explanation": "The Rex-Cantlie line (Cantlie's line) runs from the gallbladder fossa to the IVC and divides the liver into functional right and left halves. Segment IV (quadrate lobe) straddles this plane. The caudate lobe (segment I) is unique — it receives dual portal supply and drains directly into the IVC via accessory hepatic veins."},
{"id": 120, "cat": "Liver", "q": "A patient with cirrhosis and jaundice has Child-Pugh class C. Surgeons are considering hepatic resection for a 3 cm HCC. What is the most important contraindication to resection in this patient?", "source": "HPB Surgery / Hepatic Reserve", "correct": "Child-Pugh class C (severely impaired hepatic reserve; transplant is preferred)", "choices": ["Child-Pugh class C (severely impaired hepatic reserve; transplant is preferred)", "Tumor size <4 cm", "AFP >200 ng/mL", "Age >65"], "explanation": "Hepatic resection requires adequate functional reserve. Child-Pugh class A is acceptable; class B is borderline; class C is a contraindication to resection (mortality >20%). MELD score and future liver remnant volume (>25–30% in normal liver, >40% in cirrhosis) are critical. Transplant addresses both HCC and cirrhosis and is preferred for Milan criteria patients."},
{"id": 121, "cat": "Liver", "q": "A 55-year-old with known colorectal cancer develops 4 bilobar liver metastases (2 in right lobe, 2 in left lobe). Primary tumor has been resected. What determines resectability of colorectal liver metastases (CRLM)?", "source": "NCCN Colorectal Cancer Guidelines", "correct": "Ability to achieve R0 resection with adequate future liver remnant (≥20–25% of total liver volume)", "choices": ["Ability to achieve R0 resection with adequate future liver remnant (≥20–25% of total liver volume)", "Number of metastases ≤3", "Unilobar distribution only", "CEA level <200 ng/mL"], "explanation": "Resectability of CRLM is defined by ability to: achieve R0 margins, preserve adequate FLR (≥20% normal liver, ≥30% with chemotherapy-induced injury, ≥40% cirrhosis), and leave adequate vascular inflow/outflow and biliary drainage. Number, size, bilobar distribution are NOT absolute contraindications. Staged resections and portal vein embolization (to hypertrophy FLR) expand resectability."},
{"id": 122, "cat": "Liver", "q": "A pyogenic liver abscess is identified on CT. The most common causative organism in a patient with no underlying biliary disease or recent endoscopy is:", "source": "Infectious Disease / Liver Abscess", "correct": "Klebsiella pneumoniae (increasingly in Asia; E. coli elsewhere)", "choices": ["Klebsiella pneumoniae (increasingly in Asia; E. coli elsewhere)", "Entamoeba histolytica", "Streptococcus milleri", "Candida species"], "explanation": "Pyogenic liver abscesses: most common organisms include E. coli, Klebsiella (especially K. pneumoniae, associated with cryptogenic abscesses in Asia), Streptococcus milleri group, and anaerobes. Klebsiella is increasingly recognized globally and associated with endophthalmitis. Entamoeba causes amebic abscesses (usually single, right lobe, from endemic areas)."},
{"id": 123, "cat": "Liver", "q": "Amebic liver abscess (Entamoeba histolytica) versus pyogenic liver abscess — which feature most suggests amebic origin and guides treatment?", "source": "Tropical Medicine / HPB", "correct": "Travel to/from endemic area + positive serology + anchovy-paste aspirate; treat with metronidazole (surgery usually NOT needed)", "choices": ["Travel to/from endemic area + positive serology + anchovy-paste aspirate; treat with metronidazole (surgery usually NOT needed)", "Multiple abscesses + fever; requires surgical drainage", "Air-fluid level on CT; requires percutaneous drainage", "Positive blood cultures; requires antibiotics + drainage"], "explanation": "Amebic abscesses: single, large, right lobe; endemic travel history; positive E. histolytica serology; aspirate is odorless, brown 'anchovy paste.' Metronidazole (750 mg TID × 10 days) is curative in >90%; percutaneous drainage only for large abscesses at risk of rupture or metronidazole failure. Pyogenic abscesses typically require drainage + antibiotics."},
{"id": 124, "cat": "Liver", "q": "The Pringle maneuver (clamping of the hepatoduodenal ligament) achieves temporary hemostasis during liver surgery by occluding which structures?", "source": "HPB Surgical Technique", "correct": "Portal vein and hepatic artery (inflow occlusion)", "choices": ["Portal vein and hepatic artery (inflow occlusion)", "Hepatic veins and IVC (outflow occlusion)", "Portal vein only", "Hepatic artery only"], "explanation": "The Pringle maneuver clamps the hepatoduodenal ligament, occluding the portal vein and hepatic artery (hepatic inflow). Safe ischemic time: ~60 min in normal liver, ~30 min in cirrhotic liver. The bile duct is also in the ligament but clamping it has no hemostatic effect. Total hepatic vascular exclusion (THVE) additionally occludes the IVC above and below the liver."},
{"id": 125, "cat": "Liver", "q": "A 45-year-old presents with triad of right upper quadrant pain, jaundice, and fever (Charcot's triad) plus confusion and hypotension (Reynolds' pentad). What diagnosis should be treated as a surgical emergency?", "source": "Biliary Surgery / Cholangitis", "correct": "Acute suppurative (ascending) cholangitis requiring urgent biliary decompression", "choices": ["Acute suppurative (ascending) cholangitis requiring urgent biliary decompression", "Hepatic abscess requiring percutaneous drainage", "Viral hepatitis — supportive care", "Cholecystitis requiring laparoscopic cholecystectomy"], "explanation": "Reynolds' pentad (Charcot's triad + shock + confusion) indicates acute suppurative cholangitis — pus under pressure in the biliary system. This is a surgical emergency with 50% mortality if not promptly decompressed. Initial treatment: IV antibiotics + resuscitation + urgent biliary decompression (ERCP preferred; PTC or surgical drainage if ERCP unavailable)."},
{"id": 126, "cat": "Liver", "q": "Budd-Chiari syndrome is caused by obstruction of hepatic venous outflow. Which treatment provides the best long-term outcome for patients with severe Budd-Chiari not responding to anticoagulation?", "source": "EASL / Budd-Chiari Syndrome", "correct": "TIPS (transjugular intrahepatic portosystemic shunt) or liver transplantation", "choices": ["TIPS (transjugular intrahepatic portosystemic shunt) or liver transplantation", "Systemic thrombolysis alone", "Surgical portacaval shunt", "Anticoagulation indefinitely"], "explanation": "Budd-Chiari (hepatic vein/IVC thrombosis): anticoagulation is first-line. For those who fail: TIPS decompresses the liver and is preferred over surgical shunts. Liver transplant is definitive for acute liver failure or cirrhosis from chronic Budd-Chiari. Most patients have underlying prothrombotic conditions (JAK2 mutation, PNH, antiphospholipid syndrome)."},
{"id": 127, "cat": "Liver", "q": "During a right hepatectomy, which vein must be divided to fully mobilize the right lobe from the retrohepatic IVC?", "source": "Hepatic Surgery Anatomy", "correct": "Short hepatic veins (accessory right hepatic veins) draining directly into the IVC", "choices": ["Short hepatic veins (accessory right hepatic veins) draining directly into the IVC", "Right hepatic vein at its IVC junction", "Middle hepatic vein", "Portal vein bifurcation"], "explanation": "Multiple short hepatic veins drain segment VI and VII directly into the retrohepatic IVC (not via the major right hepatic vein). These must be individually ligated and divided during right hepatic mobilization. The right hepatic vein proper is divided last at the IVC. Failure to control these small veins is a common source of major hemorrhage."},
{"id": 128, "cat": "Liver", "q": "A solitary hepatic cyst is found incidentally on CT. It has smooth walls, no septa, and is anechoic on ultrasound. What is the appropriate management?", "source": "HPB Surgery / Simple Hepatic Cysts", "correct": "Observation; no intervention unless symptomatic", "choices": ["Observation; no intervention unless symptomatic", "Aspiration and sclerotherapy", "Surgical unroofing", "Liver resection"], "explanation": "Simple hepatic cysts are congenital (bile duct origin), found in ~5% of population, with no malignant potential. Observation suffices. Intervention (laparoscopic unroofing/fenestration) is reserved for symptomatic cysts (pain, early satiety, biliary compression). Aspiration alone has >80% recurrence rate; sclerotherapy reduces recurrence but is reserved for high-risk surgical patients."},
{"id": 129, "cat": "Liver", "q": "Hydatid disease (echinococcal cyst) of the liver is caused by Echinococcus granulosus. What is the critical precaution during surgical resection?", "source": "Parasitic Surgery / Hydatid Disease", "correct": "Avoid cyst rupture (anaphylaxis + peritoneal seeding); protect field with hypertonic saline-soaked packs", "choices": ["Avoid cyst rupture (anaphylaxis + peritoneal seeding); protect field with hypertonic saline-soaked packs", "Always aspirate cyst first to decompress", "Drain cyst into peritoneum safely", "No special precautions needed"], "explanation": "Hydatid cysts: spillage causes anaphylaxis (from cyst fluid) and peritoneal seeding (daughter cysts). Surgical precautions: peri-cyst packing with hypertonic saline (15–20%) or povidone-iodine scolicide, careful dissection to avoid rupture, PAIR (puncture-aspiration-injection-reaspiration) is an alternative in selected cases. Preoperative albendazole reduces recurrence."},
{"id": 130, "cat": "Liver", "q": "TIPS (transjugular intrahepatic portosystemic shunt) creates a communication between which two vessels?", "source": "Interventional Radiology / Portal Hypertension", "correct": "Hepatic vein to portal vein (intrahepatic, via stent)", "choices": ["Hepatic vein to portal vein (intrahepatic, via stent)", "Portal vein to IVC (extrahepatic)", "Hepatic artery to portal vein", "Splenic vein to renal vein"], "explanation": "TIPS creates an intrahepatic shunt connecting the portal vein to a hepatic vein via a metallic stent, reducing portal pressure. Indications: refractory variceal bleeding, refractory ascites, Budd-Chiari. Contraindications: severe hepatic encephalopathy, heart failure, pulmonary hypertension, polycystic liver, active infection. Hepatic encephalopathy is a major complication (diverts portal blood away from liver)."},
{"id": 131, "cat": "Pancreas", "q": "A patient presents with acute pancreatitis. On admission, which laboratory/clinical finding from the Ranson criteria predicts the WORST prognosis at 48 hours (not on admission)?", "source": "Ranson Criteria / Acute Pancreatitis", "correct": "Calcium <8 mg/dL at 48 hours", "choices": ["Calcium <8 mg/dL at 48 hours", "Age >55 at admission", "WBC >16,000 at admission", "AST >250 at admission"], "explanation": "Ranson criteria at 48 hours (not on admission): Ca <8 mg/dL, BUN rise >5 mg/dL, PaO2 <60 mmHg, base deficit >4 mEq/L, fluid sequestration >6L, Hct fall >10%. On admission: age >55, WBC >16K, glucose >200, LDH >350, AST >250. Hypocalcemia (saponification) at 48h correlates with severe necrotizing pancreatitis."},
{"id": 132, "cat": "Pancreas", "q": "Infected pancreatic necrosis is confirmed. Antibiotics are started. What is the preferred timing and approach for necrosectomy?", "source": "IAP/APA Acute Pancreatitis Guidelines", "correct": "Delayed (≥4 weeks) step-up approach: percutaneous drainage first, then minimally invasive necrosectomy if needed", "choices": ["Delayed (≥4 weeks) step-up approach: percutaneous drainage first, then minimally invasive necrosectomy if needed", "Immediate open necrosectomy within 48 hours", "Antibiotics alone; never operate", "Laparoscopic necrosectomy within 1 week"], "explanation": "PANTER trial established: step-up approach (percutaneous/endoscopic drainage → minimally invasive necrosectomy) is superior to open surgery, with significantly lower morbidity (new-onset organ failure, incisional hernia, diabetes). Delay of ≥4 weeks allows demarcation of necrosis. Early surgery (<2 weeks) has mortality >65%. Sterile necrosis: no intervention unless symptomatic."},
{"id": 133, "cat": "Pancreas", "q": "A 55-year-old develops a pancreatic pseudocyst 6 weeks after acute pancreatitis. It is 7 cm, causes abdominal pain, and has not resolved. What is the preferred drainage procedure?", "source": "Pancreatic Surgery Guidelines", "correct": "Endoscopic ultrasound-guided cystogastrostomy (EUS-guided internal drainage)", "choices": ["Endoscopic ultrasound-guided cystogastrostomy (EUS-guided internal drainage)", "Percutaneous external drainage", "Distal pancreatectomy", "Whipple procedure"], "explanation": "For mature pseudocysts (≥6 weeks, thick wall) adherent to stomach or duodenum: EUS-guided internal drainage (cystogastrostomy or cystoduodenostomy) is first-line — low morbidity, durable. Surgical internal drainage (cystogastrostomy/Roux-en-Y cystojejunostomy) for failed endoscopy. External percutaneous drainage for infected pseudocysts or when not adjacent to stomach. Resection is rarely needed."},
{"id": 134, "cat": "Pancreas", "q": "A 45-year-old woman presents with episodic hypoglycemia, diaphoresis, and confusion relieved by eating. Fasting glucose is 38 mg/dL with insulin 28 μU/mL and C-peptide 3.2 ng/mL. What is the diagnosis and localizing test?", "source": "Endocrine Surgery / Insulinoma", "correct": "Insulinoma; localized with EUS (most sensitive) or CT/MRI; intraoperative ultrasound at surgery", "choices": ["Insulinoma; localized with EUS (most sensitive) or CT/MRI; intraoperative ultrasound at surgery", "Factitious hypoglycemia (exogenous insulin); C-peptide would be low", "Glucagonoma; treat with somatostatin analogue", "Nesidioblastosis; no localization needed"], "explanation": "Whipple's triad: symptoms with fasting hypoglycemia + relief with glucose. Insulinoma: inappropriately elevated insulin AND C-peptide (excludes exogenous insulin). EUS is most sensitive for localization (90%). 90% benign, 90% solitary, 10% in MEN1. Treatment: enucleation (most) or distal pancreatectomy. Intraoperative ultrasound is essential — 40% not palpable at surgery."},
{"id": 135, "cat": "Pancreas", "q": "A patient with MEN1 has recurrent peptic ulcers despite PPI therapy, and serum gastrin of 1,200 pg/mL (normal <100). Secretin stimulation test shows a paradoxical rise in gastrin >200 pg/mL. What is the diagnosis and primary treatment?", "source": "Gastrinoma / ZES / MEN1", "correct": "Zollinger-Ellison syndrome (gastrinoma); high-dose PPI to control acid, surgery for sporadic but medical management in MEN1", "choices": ["Zollinger-Ellison syndrome (gastrinoma); high-dose PPI to control acid, surgery for sporadic but medical management in MEN1", "Insulinoma; treat with diazoxide", "G-cell hyperplasia; antrectomy", "Carcinoid syndrome; treat with octreotide"], "explanation": "ZES: paradoxical gastrin rise with secretin (>200 pg/mL) is diagnostic. In sporadic ZES: surgery (resection of gastrinoma) can be curative. In MEN1-associated ZES: tumors are often multiple, lymph node metastases common — surgery is controversial; medical management (PPIs + somatostatin) is standard because surgical cure rate is very low (<10% in MEN1-ZES)."},
{"id": 136, "cat": "Pancreas", "q": "A patient presents with watery diarrhea (5–10L/day), hypokalemia, and achlorhydria (WDHA syndrome). CT shows a 3 cm pancreatic tail mass. What functional tumor is most likely?", "source": "Endocrine Surgery / VIPoma", "correct": "VIPoma (Verner-Morrison syndrome)", "choices": ["VIPoma (Verner-Morrison syndrome)", "Insulinoma", "Gastrinoma", "Glucagonoma"], "explanation": "WDHA = Watery Diarrhea, Hypokalemia, Achlorhydria — pathognomonic for VIPoma (vasoactive intestinal polypeptide). Large-volume secretory diarrhea (>3 L/day), hypokalemia from GI loss, achlorhydria (VIP inhibits gastric acid). Often solitary, pancreatic tail. Confirm with serum VIP. Treatment: surgical resection; octreotide to control symptoms preoperatively."},
{"id": 137, "cat": "Pancreas", "q": "Glucagonoma classically presents with necrolytic migratory erythema, diabetes, weight loss, and anemia. Serum glucagon is >1,000 pg/mL. This tumor most commonly arises from which pancreatic cell type and where?", "source": "Endocrine Surgery / Glucagonoma", "correct": "Alpha cells of the pancreas; most commonly in the body/tail", "choices": ["Alpha cells of the pancreas; most commonly in the body/tail", "Beta cells; head of pancreas", "Delta cells; diffusely throughout pancreas", "PP cells; head of pancreas"], "explanation": "Glucagonoma arises from alpha cells, predominantly in the pancreatic body/tail. The 4 D's: Dermatitis (NME — bullous, crusting rash), Diabetes, Deep vein thrombosis, Depression (weight loss, anemia). >50% have metastases at diagnosis. Resection for localized disease; octreotide + zinc for dermatitis; anticoagulation for DVT prophylaxis."},
{"id": 138, "cat": "Pancreas", "q": "A 68-year-old has a 3 cm pancreatic head mass with biliary and pancreatic duct dilatation ('double duct sign'), jaundice, and new-onset diabetes. CT shows no vascular involvement or metastases. What is the next step?", "source": "NCCN Pancreatic Cancer Guidelines", "correct": "Proceed to Whipple (pancreaticoduodenectomy) — tissue diagnosis not required for resectable disease", "choices": ["Proceed to Whipple (pancreaticoduodenectomy) — tissue diagnosis not required for resectable disease", "EUS-FNA biopsy required before any surgery", "ERCP stenting, then reassess in 3 months", "Neoadjuvant chemoradiation first"], "explanation": "For clearly resectable pancreatic head mass with classic features (double duct sign, jaundice, weight loss), upfront surgery (Whipple) is recommended WITHOUT mandatory tissue confirmation, as biopsy may cause seeding and delays. EUS-FNA is indicated when: (1) diagnosis is uncertain, (2) neoadjuvant therapy is planned, or (3) borderline/locally advanced disease requiring confirmation before systemic therapy."},
{"id": 139, "cat": "Pancreas", "q": "A main-duct IPMN (intraductal papillary mucinous neoplasm) is found with main pancreatic duct dilation >10 mm. What is the recommended management?", "source": "Fukuoka Consensus / IAP IPMN Guidelines 2017", "correct": "Surgical resection (high risk of malignancy: ~45–60%)", "choices": ["Surgical resection (high risk of malignancy: ~45–60%)", "Observe with annual MRI", "EUS-FNA for cytology; operate only if malignant", "Pancreatectomy only if symptomatic"], "explanation": "Main-duct IPMN with MPD ≥10 mm carries ~45–60% risk of high-grade dysplasia or invasive carcinoma. Fukuoka high-risk stigmata (resect): MPD ≥10 mm, obstructive jaundice from cystic lesion, enhancing mural nodule, or cytology positive/suspicious. Branch-duct IPMN follow a different algorithm (size, worrisome features). MD-IPMN always requires surgical consultation."},
{"id": 140, "cat": "Pancreas", "q": "A 50-year-old woman has a cystic pancreatic lesion. MRI shows a multiloculated cyst in the tail with ovarian-type stroma on biopsy and elevated CEA in cyst fluid (>192 ng/mL). What is the diagnosis and treatment?", "source": "Pancreatic Cystic Neoplasm Guidelines", "correct": "Mucinous cystic neoplasm (MCN); resection recommended (malignant potential)", "choices": ["Mucinous cystic neoplasm (MCN); resection recommended (malignant potential)", "Serous cystadenoma; observation", "Pseudocyst; external drainage", "IPMN; follow per Fukuoka guidelines"], "explanation": "MCN: almost exclusively in women (>95%), tail/body, no communication with pancreatic duct, ovarian stroma (diagnostic), high CEA in fluid. Malignancy risk ~10–17%. Resection recommended for all surgical candidates. Contrast with serous cystadenoma (honeycomb appearance, low CEA, benign, observe) and pseudocyst (history of pancreatitis, no stroma)."},
{"id": 141, "cat": "Pancreas", "q": "After Whipple procedure, the patient develops high-output drain amylase (>3× serum amylase) on postoperative day 3, without clinical deterioration. What is the most appropriate initial management of this Grade A postoperative pancreatic fistula (POPF)?", "source": "ISGPF / Pancreatic Fistula Guidelines", "correct": "Conservative management: maintain drain, low-fat diet or bowel rest, observe", "choices": ["Conservative management: maintain drain, low-fat diet or bowel rest, observe", "Immediate re-operation", "Octreotide infusion and NPO", "Percutaneous drainage of new collection"], "explanation": "ISGPF Grade A POPF (biochemical leak): high drain amylase >3× serum, no clinical impact, no change in management needed beyond maintaining the drain. Grade B: clinical impact, drain maintained, NPO ± octreotide, may need interventional drainage. Grade C: life-threatening, requires reoperation. Most POPFs (especially Grade A/B) resolve with conservative management."},
{"id": 142, "cat": "Pancreas", "q": "Pancreas divisum results from failure of fusion of the dorsal and ventral pancreatic buds. Which duct carries the majority of pancreatic secretion in pancreas divisum, and through which papilla?", "source": "Pancreatic Anatomy / Pancreas Divisum", "correct": "Dorsal duct (duct of Santorini) drains through the minor papilla", "choices": ["Dorsal duct (duct of Santorini) drains through the minor papilla", "Ventral duct (duct of Wirsung) drains through the minor papilla", "Both ducts drain through the major papilla", "Dorsal duct drains through the major papilla"], "explanation": "In pancreas divisum (most common pancreatic anatomical variant, ~7%), the dorsal and ventral buds fail to fuse. The dorsal duct (Santorini, which drains the body/tail and superior head) drains through the minor papilla. The ventral duct (Wirsung, draining the inferior head) drains through the major papilla. The small minor papilla may cause relative obstruction → recurrent acute pancreatitis."},
{"id": 143, "cat": "Pancreas", "q": "A 45-year-old with chronic alcohol-related pancreatitis has a dilated main pancreatic duct (>7 mm) with a 'chain of lakes' appearance on MRCP. He has intractable pain. Which surgical procedure is most appropriate?", "source": "Chronic Pancreatitis Surgery", "correct": "Lateral pancreaticojejunostomy (Puestow procedure / modified Partington-Rochelle)", "choices": ["Lateral pancreaticojejunostomy (Puestow procedure / modified Partington-Rochelle)", "Whipple procedure (pancreaticoduodenectomy)", "Distal pancreatectomy", "Total pancreatectomy with islet autotransplantation"], "explanation": "For large-duct chronic pancreatitis (MPD >7 mm): lateral pancreaticojejunostomy (Puestow/modified Partington-Rochelle) provides pain relief in 70–80% by draining the dilated duct into a Roux limb along its entire length. Whipple is reserved for dominant head disease (Beger, Frey procedures also option). Distal pancreatectomy if disease limited to tail. TPIAT is for small-duct or failed prior surgery."},
{"id": 144, "cat": "Pancreas", "q": "A trauma patient undergoes CT showing transaction of the pancreatic body at the neck, with injury to the main pancreatic duct. What is the critical feature that determines operative management of pancreatic injuries?", "source": "AAST / Pancreatic Trauma", "correct": "Main pancreatic duct integrity — ductal disruption requires operative drainage or distal resection", "choices": ["Main pancreatic duct integrity — ductal disruption requires operative drainage or distal resection", "Serum amylase level", "Pancreatic contusion size on CT", "Mechanism of injury"], "explanation": "The most important factor in pancreatic injury is ductal involvement. AAST grade I–II (no ductal injury): drainage and observation. Grade III (distal ductal injury, left of SMA): distal pancreatectomy. Grade IV (ductal injury at head): consider damage control, external drainage, and delayed Whipple or Roux-en-Y drainage. Serum amylase is insensitive early; ERCP/MRCP confirms duct integrity."},
{"id": 145, "cat": "Pancreas", "q": "Somatostatinoma is the rarest functional pancreatic endocrine tumor. It classically presents with the 'inhibitory syndrome' — which triad?", "source": "Endocrine Surgery / Somatostatinoma", "correct": "Diabetes, cholelithiasis, and steatorrhea (diarrhea)", "choices": ["Diabetes, cholelithiasis, and steatorrhea (diarrhea)", "Hypoglycemia, weight loss, and diarrhea", "Peptic ulcer disease, diarrhea, and elevated gastrin", "Hypertension, headache, and diaphoresis"], "explanation": "Somatostatin inhibits: insulin (→ diabetes), cholecystokinin-driven gallbladder contraction (→ cholelithiasis), exocrine pancreatic secretion (→ fat malabsorption/steatorrhea), and gastric acid (→ hypochlorhydria). Somatostatinomas are usually in the pancreatic head or periampullary region. Most malignant at diagnosis. Treatment: resection if possible; octreotide for symptoms."},
{"id": 146, "cat": "Trauma", "q": "A trauma patient arrives in hemorrhagic shock. The FAST exam is positive in the right upper quadrant (Morrison's pouch). After 2L crystalloid, BP is 60/40 and HR 130. What is the most appropriate next step?", "source": "ATLS 10th Edition", "correct": "Emergency laparotomy (operative hemorrhage control — patient is non-responder)", "choices": ["Emergency laparotomy (operative hemorrhage control — patient is non-responder)", "CT scan of abdomen/pelvis", "Repeat FAST exam", "Angioembolization"], "explanation": "Non-responders to initial resuscitation (BP does not normalize with 2L crystalloid + blood) with positive FAST require immediate laparotomy. CT is only for hemodynamically stable patients. Non-responder = ongoing hemorrhage; delay for CT is lethal. FAST positive + unstable = OR now. ATLS principle: airway → breathing → circulation (operative control)."},
{"id": 147, "cat": "Trauma", "q": "The damage control surgery (DCS) philosophy for exsanguinating trauma involves three stages. Which of these correctly describes Stage 1?", "source": "ATLS / Damage Control Surgery", "correct": "Abbreviated laparotomy: hemorrhage control, contamination control, temporary abdominal closure (no definitive repair)", "choices": ["Abbreviated laparotomy: hemorrhage control, contamination control, temporary abdominal closure (no definitive repair)", "Definitive repair of all injuries at initial operation", "ICU resuscitation to correct the 'lethal triad' only", "Planned re-exploration and definitive repair"], "explanation": "DCS Stage 1: abbreviated laparotomy — control hemorrhage (packing, ligation, shunts), control contamination (bowel stapling), temporary abdominal closure. Stage 2: ICU resuscitation — correct lethal triad (hypothermia, acidosis, coagulopathy). Stage 3: planned re-exploration (24–48h) for definitive repair when physiology normalized. Lethal triad: temperature <35°C, pH <7.2, PT >16s."},
{"id": 148, "cat": "Trauma", "q": "The 'lethal triad' in trauma surgery refers to which three physiologic derangements that must be corrected in the ICU after damage control surgery?", "source": "Damage Control Resuscitation", "correct": "Hypothermia, acidosis, and coagulopathy", "choices": ["Hypothermia, acidosis, and coagulopathy", "Hypoxia, hypovolemia, and hyperkalemia", "Anemia, thrombocytopenia, and hypocalcemia", "Sepsis, ARDS, and renal failure"], "explanation": "The lethal triad (trauma triad of death): hypothermia (<35°C), acidosis (pH <7.2 / BE <−6), and coagulopathy (INR >1.5/PT >16s). These are self-perpetuating — each worsens the others. DCS philosophy: stop operating early to allow ICU correction. Damage control resuscitation: balanced transfusion (1:1:1 PRBCs:FFP:platelets), permissive hypotension until hemorrhage controlled."},
{"id": 149, "cat": "Trauma", "q": "A 22-year-old sustains a gunshot wound to the abdomen. At laparotomy, a segment of small bowel has three perforations over 10 cm. The colon has a single through-and-through injury near the sigmoid. What is appropriate management of the colon injury?", "source": "EAST Colon Injury Guidelines", "correct": "Primary repair (for non-destructive wounds without fecal contamination or hemodynamic instability)", "choices": ["Primary repair (for non-destructive wounds without fecal contamination or hemodynamic instability)", "Always divert with colostomy for all colon injuries", "Hartmann's procedure for all gunshot colon wounds", "Damage control: staple and defer decision"], "explanation": "EAST guidelines: primary repair is safe for non-destructive colon injuries (<50% circumference, no devascularization) in hemodynamically stable patients. Fecal diversion (Hartmann's or loop colostomy) for: destructive wounds, massive fecal contamination, significant delay to OR, hemodynamic instability, or DCS setting. Single through-and-through = non-destructive → primary repair appropriate."},
{"id": 150, "cat": "Trauma", "q": "Abdominal compartment syndrome (ACS) is defined as sustained intra-abdominal pressure >20 mmHg with new organ dysfunction. What is the definitive treatment?", "source": "WSACS / Abdominal Compartment Syndrome", "correct": "Surgical decompressive laparotomy", "choices": ["Surgical decompressive laparotomy", "Aggressive diuresis with furosemide", "Paracentesis", "Nasogastric decompression"], "explanation": "ACS: IAP >20 mmHg + new organ dysfunction (oliguria, respiratory failure, ↑peak airway pressures, decreased cardiac output). Definitive treatment: decompressive laparotomy with open abdomen management. Medical measures (NG decompression, diuresis, positioning) may temporize Grade I–II (IAP 12–20) but are insufficient for Grade IV ACS. Normal IAP <12 mmHg."},
{"id": 151, "cat": "Trauma", "q": "An unstable trauma patient has Zone 1 (central) retroperitoneal hematoma from blunt trauma found at laparotomy. What is the most appropriate management?", "source": "ATLS / Retroperitoneal Hematoma", "correct": "Always explore Zone 1 hematomas (aorta/IVC/mesenteric vessels at risk)", "choices": ["Always explore Zone 1 hematomas (aorta/IVC/mesenteric vessels at risk)", "Observe; all retroperitoneal hematomas should be packed and left alone", "Explore only if expanding", "Angioembolize intraoperatively"], "explanation": "Retroperitoneal hematoma zones: Zone 1 (central, medial) = always explore (major vessels: aorta, IVC, superior mesenteric vessels). Zone 2 (flank/lateral) = penetrating: always explore; blunt: explore if expanding. Zone 3 (pelvic) = penetrating: explore; blunt: do NOT explore (packing effective, opening disrupts tamponade). Zone 1 blunt or penetrating: control aorta at diaphragm first."},
{"id": 152, "cat": "Trauma", "q": "A pelvic ring fracture from high-energy blunt trauma causes massive retroperitoneal hemorrhage. After pre-peritoneal pelvic packing and pelvic binder application, hemostasis is inadequate. What is the next intervention?", "source": "Pelvic Trauma / EAST Guidelines", "correct": "Angioembolization (arterial source in ~15% of pelvic fracture bleeding)", "choices": ["Angioembolization (arterial source in ~15% of pelvic fracture bleeding)", "Immediate exploratory laparotomy", "External fixation only", "REBOA (Resuscitative Endovascular Balloon Occlusion of the Aorta)"], "explanation": "Pelvic fracture hemorrhage: 85% venous (pre-peritoneal packing is primary hemostasis), 15% arterial. After pelvic stabilization (binder, external fixator) and pre-peritoneal packing, angioembolization addresses arterial bleeding (superior gluteal, internal pudendal, obturator arteries). REBOA Zone III can temporize while preparing for angiography. External fixation alone is insufficient for hemostasis."},
{"id": 153, "cat": "Trauma", "q": "Blunt duodenal injury can result in an intramural hematoma that causes gastric outlet obstruction. What is the initial non-operative treatment?", "source": "Trauma Surgery / Duodenal Injuries", "correct": "NPO, nasogastric decompression, TPN for 2–3 weeks (most resolve spontaneously)", "choices": ["NPO, nasogastric decompression, TPN for 2–3 weeks (most resolve spontaneously)", "Immediate operative evacuation of hematoma", "Duodenal exclusion procedure", "Gastrojejunostomy bypass"], "explanation": "Duodenal intramural hematoma from blunt trauma (child abuse: classic, bicycle handlebars, seatbelt): most resolve with conservative management (NPO, NG, TPN) over 2–3 weeks. Surgical exploration for: failure to resolve after 3 weeks, concern for perforation, or associated injuries. Operative evacuation of hematoma is performed laparoscopically or open if conservative management fails."},
{"id": 154, "cat": "Trauma", "q": "A penetrating abdominal trauma patient undergoes laparotomy and is found to have an extraperitoneal rectal injury (below peritoneal reflection). What are the operative principles?", "source": "Trauma Surgery / Rectal Injuries", "correct": "Diverting sigmoid colostomy + presacral drainage + distal rectal washout (4 D's historically)", "choices": ["Diverting sigmoid colostomy + presacral drainage + distal rectal washout (4 D's historically)", "Primary repair of rectum without diversion", "Abdominoperineal resection", "Observation alone"], "explanation": "Extraperitoneal rectal injuries: historically required 4D's (Diversion, Distal washout, Drainage, Debridement). Modern evidence supports diverting colostomy + presacral drainage as most critical; distal washout is no longer mandatory per some guidelines. Primary repair alone is insufficient due to fecal contamination risk in extraperitoneal location. Diversion protects the repair and prevents septic complications."},
{"id": 155, "cat": "Trauma", "q": "A 25-year-old sustains a stab wound to Zone II of the neck (between cricoid cartilage and angle of mandible). He is hemodynamically stable with no hard signs of vascular injury. What is the current management approach?", "source": "Neck Trauma / EAST Guidelines", "correct": "CT angiography of the neck (selective surgical exploration based on imaging)", "choices": ["CT angiography of the neck (selective surgical exploration based on imaging)", "Mandatory operative exploration of all Zone II penetrating neck wounds", "Observation only", "Angiography and embolization"], "explanation": "Historical management: mandatory exploration of all Zone II penetrating neck injuries. Current evidence-based approach: CT angiography (±esophagoscopy/laryngoscopy) for hemodynamically stable patients without hard signs. Hard signs (active hemorrhage, expanding hematoma, bruit/thrill, neurologic deficit, tracheal deviation, subcutaneous air) → immediate OR. Selective exploration based on CTA reduces negative neck explorations."},
{"id": 156, "cat": "Trauma", "q": "A trauma patient with blunt thoracic aortic injury (BTAI) is hemodynamically stable on CT showing a Grade II aortic injury (intimal tear without hematoma). What is the recommended management?", "source": "SVS BTAI Guidelines 2011", "correct": "Medical management (heart rate and BP control) with serial imaging; TEVAR for higher grades", "choices": ["Medical management (heart rate and BP control) with serial imaging; TEVAR for higher grades", "Immediate open surgical repair", "Immediate TEVAR (thoracic endovascular aortic repair)", "Observation without antihypertensives"], "explanation": "SVS BTAI grading: Grade I (intimal tear) → medical management. Grade II (intramural hematoma) → medical vs TEVAR. Grade III (pseudoaneurysm) → TEVAR. Grade IV (rupture) → TEVAR emergently. TEVAR has largely replaced open repair (lower mortality and paraplegia rates). Anti-impulse therapy (beta blockade, target HR <60, SBP <100) is critical while planning definitive repair."},
{"id": 157, "cat": "Trauma", "q": "A patient has a diaphragmatic injury diagnosed at laparotomy for penetrating trauma. The laceration is 3 cm on the left side. What is the repair and why is the LEFT side more commonly injured?", "source": "Trauma Surgery / Diaphragm", "correct": "Primary repair with non-absorbable suture; left side more commonly diagnosed (right is buffered by liver)", "choices": ["Primary repair with non-absorbable suture; left side more commonly diagnosed (right is buffered by liver)", "Chest tube alone is sufficient; no repair needed", "Right side is more common due to aortic proximity", "Prosthetic mesh repair always required"], "explanation": "Diaphragmatic injuries: left-sided injuries are more commonly diagnosed (2:1 ratio) because the right hemidiaphragm is supported by the liver, which acts as a natural buffer and tamponades small right-sided injuries. Left-sided injuries also lead to herniation of abdominal contents (stomach, colon) visible on CXR. Repair: primary closure with non-absorbable suture (polypropylene); mesh for large defects."},
{"id": 158, "cat": "Trauma", "q": "A 30-year-old pedestrian struck by a car has a pelvic CT showing a bladder injury with contrast extravasation outside the peritoneum. What is the management of this extraperitoneal bladder rupture?", "source": "Urology / Bladder Trauma", "correct": "Urethral (Foley) catheter drainage for 10–14 days (most heal without surgery)", "choices": ["Urethral (Foley) catheter drainage for 10–14 days (most heal without surgery)", "Immediate operative repair", "Suprapubic cystostomy alone", "Observation without catheter"], "explanation": "Bladder rupture types: (1) Extraperitoneal — most common (85%), caused by pelvic fractures; managed with Foley catheter drainage alone for 10–14 days; >90% heal. (2) Intraperitoneal — caused by blunt force to full bladder; requires operative repair (urine in peritoneum → chemical peritonitis). Both types: perform cystogram before catheter removal."},
{"id": 159, "cat": "Trauma", "q": "During trauma laparotomy, a small bowel mesenteric injury is found with 30 cm of ischemic small bowel and no other injuries. The patient is hemodynamically stable. What is the appropriate management?", "source": "Trauma Surgery / Small Bowel", "correct": "Resection of ischemic bowel with primary anastomosis (if stable; no contamination)", "choices": ["Resection of ischemic bowel with primary anastomosis (if stable; no contamination)", "Damage control: staple bowel ends, return in 24–48 hours", "Leave bowel in situ and re-explore in 24 hours", "Bowel resection with end-ostomy only"], "explanation": "In hemodynamically stable trauma patients with small bowel ischemia: resect and perform primary anastomosis (safe if no contamination, no bowel wall edema, hemodynamically stable). Damage control (staple without anastomosis) reserved for DCS indications: hemodynamic instability, hypothermia, acidosis, coagulopathy, massive contamination. Primary anastomosis success rate >95% in stable patients."},
{"id": 160, "cat": "Trauma", "q": "REBOA (Resuscitative Endovascular Balloon Occlusion of the Aorta) placed in Zone III is used for which indication?", "source": "REBOA / Endovascular Trauma", "correct": "Non-compressible pelvic/junctional hemorrhage to achieve temporary hemostasis", "choices": ["Non-compressible pelvic/junctional hemorrhage to achieve temporary hemostasis", "Thoracic aortic rupture", "Splenic trauma", "Cardiac tamponade"], "explanation": "REBOA zones: Zone I (descending thoracic aorta, between subclavian and celiac) for abdominal/thoracic hemorrhage; Zone III (infrarenal aorta, above iliac bifurcation) for pelvic/junctional hemorrhage. Zone II is avoided (visceral vessel origin). Zone III REBOA provides temporizing hemorrhage control for pelvic fracture bleeding while patient moves to angiography or OR. Reduces end-organ ischemia vs thoracotomy/aortic cross-clamp."}
]

REF = [
  {
    "topic": "Hernia",
    "color": "#1A3C6E",
    "sections": [
      {
        "title": "Hiatal Hernia Types",
        "table": {
          "headers": [
            "Type",
            "Description",
            "Surgery?"
          ],
          "rows": [
            [
              "I — Sliding",
              "GEJ slides above diaphragm (95%)",
              "Symptomatic only"
            ],
            [
              "II — Paraesophageal",
              "GEJ normal, fundus herniates",
              "Yes — volvulus risk"
            ],
            [
              "III — Mixed",
              "GEJ + fundus both herniate",
              "Yes"
            ],
            [
              "IV — Giant",
              "Other organs (colon, spleen)",
              "Urgent if symptoms"
            ]
          ]
        }
      },
      {
        "title": "Anti-Reflux Procedures",
        "table": {
          "headers": [
            "Procedure",
            "Wrap",
            "Indication"
          ],
          "rows": [
            [
              "Nissen",
              "360° total",
              "Normal peristalsis"
            ],
            [
              "Toupet",
              "270° posterior",
              "Weak peristalsis"
            ],
            [
              "Dor",
              "Anterior 180°",
              "After Heller myotomy"
            ]
          ]
        }
      },
      {
        "title": "Inguinal Hernia Repair Options",
        "table": {
          "headers": [
            "Repair",
            "Type",
            "Key Point"
          ],
          "rows": [
            [
              "Lichtenstein",
              "Open mesh",
              "Gold standard, tension-free"
            ],
            [
              "TEP",
              "Laparoscopic",
              "Extraperitoneal — no bowel risk"
            ],
            [
              "TAPP",
              "Laparoscopic",
              "Transabdominal — bilateral easier"
            ],
            [
              "Shouldice",
              "Open non-mesh",
              "Low recurrence without mesh"
            ],
            [
              "McVay",
              "Open",
              "Only one that covers femoral space"
            ]
          ]
        }
      },
      {
        "title": "Eponymous Hernias",
        "table": {
          "headers": [
            "Name",
            "Content / Location"
          ],
          "rows": [
            [
              "Richter's",
              "Partial bowel wall only (antimesenteric)"
            ],
            [
              "Littre's",
              "Meckel's diverticulum"
            ],
            [
              "Amyand's",
              "Appendix in inguinal hernia sac"
            ],
            [
              "Maydl's",
              "W-loop of bowel (intervening loop ischemic)"
            ],
            [
              "Spigelian",
              "Through linea semilunaris, below arcuate line"
            ],
            [
              "Obturator",
              "Through obturator foramen — Howship-Romberg sign"
            ],
            [
              "Grynfeltt",
              "Superior lumbar triangle (more common)"
            ],
            [
              "Petit's",
              "Inferior lumbar triangle"
            ]
          ]
        }
      }
    ]
  },
  {
    "topic": "Appendicitis",
    "color": "#7B1FA2",
    "sections": [
      {
        "title": "Scoring Systems",
        "table": {
          "headers": [
            "Score",
            "Components",
            "Cut-off"
          ],
          "rows": [
            [
              "Alvarado (MANTRELS)",
              "Migration, Anorexia, N/V, Tenderness RLQ, Rebound, Temp, WBC, Shift",
              "≥7 = high probability"
            ],
            [
              "Pediatric Appendicitis Score (PAS)",
              "8 items including jumping/cough",
              "≥6 = likely appy"
            ],
            [
              "AIR Score",
              "7 items including CRP",
              "1-4 low, 5-8 medium, 9-12 high"
            ]
          ]
        }
      },
      {
        "title": "Management by Presentation",
        "table": {
          "headers": [
            "Presentation",
            "Management"
          ],
          "rows": [
            [
              "Uncomplicated",
              "Lap appendectomy (or antibiotics alone per APPAC)"
            ],
            [
              "Gangrenous",
              "Lap appendectomy + peritoneal washout"
            ],
            [
              "Phlegmon (no abscess)",
              "Immediate surgery"
            ],
            [
              "Abscess <3cm",
              "IV antibiotics alone, monitor"
            ],
            [
              "Abscess ≥3cm",
              "Percutaneous drain + antibiotics → interval appy 6-12 wks"
            ],
            [
              "Diffuse peritonitis",
              "Emergency lap/open appendectomy"
            ]
          ]
        }
      },
      {
        "title": "Appendiceal Neoplasms",
        "table": {
          "headers": [
            "Type",
            "Frequency",
            "Treatment"
          ],
          "rows": [
            [
              "Carcinoid <2cm",
              "Most common (50%)",
              "Appendectomy alone"
            ],
            [
              "Carcinoid >2cm",
              "",
              "Right hemicolectomy"
            ],
            [
              "Mucocele/LAMN",
              "",
              "Careful appendectomy (no rupture)"
            ],
            [
              "Adenocarcinoma",
              "",
              "Right hemicolectomy"
            ],
            [
              "Pseudomyxoma peritonei",
              "Complication of LAMN rupture",
              "CRS + HIPEC"
            ]
          ]
        }
      }
    ]
  },
  {
    "topic": "Skin & STS",
    "color": "#BF360C",
    "sections": [
      {
        "title": "Melanoma Excision Margins",
        "table": {
          "headers": [
            "Breslow Thickness",
            "Margin"
          ],
          "rows": [
            [
              "In situ",
              "0.5 – 1 cm"
            ],
            [
              "<1 mm",
              "1 cm"
            ],
            [
              "1–2 mm",
              "1–2 cm"
            ],
            [
              ">2 mm",
              "2 cm"
            ]
          ]
        }
      },
      {
        "title": "Melanoma Staging (T category)",
        "table": {
          "headers": [
            "T Stage",
            "Thickness",
            "Ulceration"
          ],
          "rows": [
            [
              "T1a",
              "<0.8mm",
              "No"
            ],
            [
              "T1b",
              "<0.8mm with ulc OR 0.8–1mm",
              "±"
            ],
            [
              "T2a",
              "1.0–2.0mm",
              "No"
            ],
            [
              "T2b",
              "1.0–2.0mm",
              "Yes"
            ],
            [
              "T3a",
              "2.0–4.0mm",
              "No"
            ],
            [
              "T3b",
              "2.0–4.0mm",
              "Yes"
            ],
            [
              "T4a",
              ">4.0mm",
              "No"
            ],
            [
              "T4b",
              ">4.0mm",
              "Yes"
            ]
          ]
        }
      },
      {
        "title": "STS: Management by Stage",
        "table": {
          "headers": [
            "Grade",
            "Size",
            "Treatment"
          ],
          "rows": [
            [
              "Low grade",
              "Any size",
              "Wide excision alone"
            ],
            [
              "High grade",
              "<5cm",
              "Wide excision ± radiation"
            ],
            [
              "High grade",
              ">5cm",
              "Surgery + radiation + consider chemo"
            ],
            [
              "Retroperitoneal",
              "Usually large",
              "En bloc resection, preop radiation preferred"
            ],
            [
              "Unresectable/metastatic",
              "",
              "Doxorubicin + ifosfamide"
            ]
          ]
        }
      },
      {
        "title": "Notable STS Types",
        "table": {
          "headers": [
            "Type",
            "Key Feature",
            "Treatment"
          ],
          "rows": [
            [
              "Liposarcoma",
              "Most common RPS",
              "Wide resection"
            ],
            [
              "Leiomyosarcoma",
              "Smooth muscle; GI/uterus/retro",
              "Resection"
            ],
            [
              "Synovial sarcoma",
              "Young adults; SS18 translocation",
              "Wide excision + XRT"
            ],
            [
              "DFSP",
              "CD34+; t(17;22); low met risk",
              "Mohs or 2–3cm margins"
            ],
            [
              "Desmoid",
              "No mets; FAP-assoc",
              "Watch → medical → surgery last"
            ],
            [
              "Rhabdomyosarcoma",
              "Children; most common pediatric STS",
              "Multimodal"
            ]
          ]
        }
      }
    ]
  },
  {
    "topic": "Thyroid",
    "color": "#00695C",
    "sections": [
      {
        "title": "PTU vs Methimazole (MMI)",
        "table": {
          "headers": [
            "Feature",
            "PTU",
            "MMI"
          ],
          "rows": [
            [
              "1st trimester",
              "Preferred",
              "Avoid (aplasia cutis)"
            ],
            [
              "2nd/3rd trimester",
              "Avoid (hepatotoxicity)",
              "Preferred"
            ],
            [
              "Thyroid storm",
              "Yes (blocks T4→T3)",
              "No"
            ],
            [
              "Dosing",
              "3× daily",
              "Once daily"
            ]
          ]
        }
      },
      {
        "title": "Thyroid Storm: Order of Treatment",
        "table": {
          "headers": [
            "Step",
            "Drug",
            "Mechanism"
          ],
          "rows": [
            [
              "1st",
              "PTU 600mg load → 200mg q8h",
              "Blocks synthesis + T4→T3"
            ],
            [
              "2nd",
              "Hydrocortisone 300mg IV",
              "Blocks conversion, adrenal support"
            ],
            [
              "3rd (1hr after PTU)",
              "Lugol's iodine / SSKI",
              "Wolff-Chaikoff, ↓ release"
            ],
            [
              "4th",
              "Propranolol 60-80mg q4h",
              "HR control, blocks T4→T3"
            ],
            [
              "5th",
              "Supportive",
              "Cool, fluids, treat precipitant"
            ]
          ]
        }
      },
      {
        "title": "Types of Thyroiditis",
        "table": {
          "headers": [
            "Type",
            "Key Feature",
            "Treatment"
          ],
          "rows": [
            [
              "Hashimoto's",
              "TPO Ab; lymphoma risk",
              "Thyroxine"
            ],
            [
              "de Quervain's",
              "Viral; painful; ESR↑",
              "NSAIDs, steroids"
            ],
            [
              "Silent/Painless",
              "Autoimmune; self-limited",
              "Observation"
            ],
            [
              "Postpartum",
              "6wks-6mo post delivery",
              "Observation ± T4"
            ],
            [
              "Suppurative",
              "Bacterial; fluctuant",
              "I&D + antibiotics"
            ],
            [
              "Riedel's",
              "IgG4; iron-hard; fibrous",
              "Tamoxifen + steroids"
            ]
          ]
        }
      }
    ]
  },
  {
    "topic": "Parathyroid",
    "color": "#E65100",
    "sections": [
      {
        "title": "Hyperparathyroidism Types",
        "table": {
          "headers": [
            "Type",
            "Ca²⁺",
            "PTH",
            "Cause"
          ],
          "rows": [
            [
              "Primary",
              "↑↑",
              "↑↑",
              "Adenoma (85%), hyperplasia, carcinoma"
            ],
            [
              "Secondary",
              "Low/normal",
              "↑↑",
              "CKD (↓ Ca → ↑ PTH)"
            ],
            [
              "Tertiary",
              "↑",
              "↑↑",
              "Autonomous PTH after long secondary"
            ],
            [
              "FHH",
              "↑ (mild)",
              "Normal/mild↑",
              "CaSR mutation — CCCR <0.01"
            ]
          ]
        }
      },
      {
        "title": "2022 Indications for Parathyroidectomy",
        "table": {
          "headers": [
            "Criterion",
            "Threshold"
          ],
          "rows": [
            [
              "Serum calcium",
              ">1.0 mg/dL above upper normal limit"
            ],
            [
              "Age",
              "<50 years"
            ],
            [
              "Bone density",
              "T-score ≤-2.5 at any site OR vertebral fracture"
            ],
            [
              "Urine calcium",
              ">400 mg/day with high stone risk"
            ],
            [
              "Renal function",
              "CrCl <60 mL/min"
            ],
            [
              "Kidney stones",
              "Nephrolithiasis or nephrocalcinosis"
            ],
            [
              "Bone loss",
              ">20% loss over 5 years"
            ]
          ]
        }
      },
      {
        "title": "MEN Syndromes",
        "table": {
          "headers": [
            "Syndrome",
            "Gene",
            "Manifestations"
          ],
          "rows": [
            [
              "MEN1",
              "MENIN (11q13)",
              "Parathyroid (95%) + Pituitary + Pancreas"
            ],
            [
              "MEN2A",
              "RET (codon 634)",
              "MTC + Pheo + Parathyroid"
            ],
            [
              "MEN2B",
              "RET (codon 918)",
              "MTC + Pheo + Marfanoid + Neuromas"
            ],
            [
              "MEN4",
              "CDKN1B (p27)",
              "MEN1-like; rare"
            ]
          ]
        }
      }
    ]
  },
  {
    "topic": "Breast/Pregnancy",
    "color": "#880E4F",
    "sections": [
      {
        "title": "Imaging Safety in Pregnancy",
        "table": {
          "headers": [
            "Modality",
            "Safety",
            "Notes"
          ],
          "rows": [
            [
              "Ultrasound",
              "✓ Safe",
              "First-line"
            ],
            [
              "Mammogram",
              "✓ Safe",
              "With abdominal shielding"
            ],
            [
              "MRI (no Gd)",
              "✓ Safe",
              "No gadolinium"
            ],
            [
              "Gadolinium MRI",
              "⚠️ Avoid",
              "Category C"
            ],
            [
              "PET/CT",
              "✗ Avoid",
              "Radiation + FDG risk"
            ],
            [
              "Bone scan",
              "✗ Avoid",
              "Avoid unless bony mets suspected"
            ]
          ]
        }
      },
      {
        "title": "Drug Safety Quick Reference",
        "table": {
          "headers": [
            "Drug",
            "Pregnancy",
            "Notes"
          ],
          "rows": [
            [
              "Doxorubicin (AC)",
              "✓ 2nd/3rd tri",
              "Preferred backbone"
            ],
            [
              "Cyclophosphamide",
              "✓ 2nd/3rd tri",
              "Part of AC"
            ],
            [
              "Taxanes",
              "⚠️ Caution",
              "Limited data"
            ],
            [
              "Trastuzumab",
              "✗ Contraindicated",
              "Oligohydramnios"
            ],
            [
              "Tamoxifen",
              "✗ Contraindicated",
              "Teratogenic"
            ],
            [
              "Methotrexate",
              "✗ Contraindicated",
              "Abortifacient"
            ],
            [
              "Tc-99m (SLNB)",
              "✓ Safe",
              "Only approved tracer"
            ],
            [
              "Blue dye (SLNB)",
              "✗ Contraindicated",
              "Anaphylaxis + fetal harm"
            ]
          ]
        }
      }
    ]
  },
  {
    "topic": "BDI",
    "color": "#1B5E20",
    "sections": [
      {
        "title": "Strasberg-Bismuth Classification",
        "table": {
          "headers": [
            "Type",
            "Description",
            "Management"
          ],
          "rows": [
            [
              "A",
              "Cystic duct leak / small duct from GB fossa",
              "ERCP stent ± drain"
            ],
            [
              "B",
              "Occluded/clipped right sectoral duct",
              "Biliary-enteric anastomosis"
            ],
            [
              "C",
              "Transected right sectoral duct (leaking)",
              "Biliary-enteric anastomosis"
            ],
            [
              "D",
              "Lateral injury to CHD/CBD",
              "Stent + primary repair"
            ],
            [
              "E1",
              "CHD transection ≥2cm from confluence",
              "Roux-en-Y HJ"
            ],
            [
              "E2",
              "CHD transection <2cm from confluence",
              "Roux-en-Y HJ"
            ],
            [
              "E3",
              "At hepatic confluence",
              "Roux-en-Y HJ"
            ],
            [
              "E4",
              "Right + left hepatic duct separation",
              "Roux-en-Y HJ (complex)"
            ],
            [
              "E5",
              "E1-4 + right hepatic duct injury",
              "HPB referral"
            ]
          ]
        }
      },
      {
        "title": "Critical View of Safety (CVS)",
        "table": {
          "headers": [
            "Requirement",
            "Detail"
          ],
          "rows": [
            [
              "1. Two structures only",
              "Cystic duct AND cystic artery — nothing else entering GB"
            ],
            [
              "2. Triangle cleared",
              "Hepatocystic triangle free of fat and fibrous tissue"
            ],
            [
              "3. GB separated",
              "Lower 1/3 of GB dissected free from liver bed"
            ]
          ]
        }
      }
    ]
  },
  {
    "topic": "Hereditary Syndromes",
    "color": "#4527A0",
    "sections": [
      {
        "title": "Quick Reference: Major Hereditary Cancer Syndromes",
        "table": {
          "headers": [
            "Syndrome",
            "Gene",
            "Key Cancers",
            "Key Feature"
          ],
          "rows": [
            [
              "BRCA1",
              "BRCA1 (17q)",
              "Breast (TNBC), Ovarian, Pancreatic",
              "TNBC pattern"
            ],
            [
              "BRCA2",
              "BRCA2 (13q)",
              "Breast (M+F), Ovarian, Pancreatic, Prostate",
              "Male breast CA"
            ],
            [
              "Lynch",
              "MLH1/MSH2/MSH6/PMS2",
              "CRC, Endometrial, Ovarian",
              "Amsterdam II criteria"
            ],
            [
              "FAP",
              "APC (5q21)",
              "CRC (100% by 40), Duodenum",
              "Prophylactic colectomy"
            ],
            [
              "Gardner",
              "APC",
              "FAP + Osteomas + Desmoids + CHRPE",
              "FAP variant"
            ],
            [
              "MEN1",
              "MENIN (11q13)",
              "PTH, Pituitary, Pancreas",
              "3 P's"
            ],
            [
              "MEN2A",
              "RET",
              "MTC, Pheo, PTH",
              "Sipple syndrome"
            ],
            [
              "MEN2B",
              "RET codon 918",
              "MTC, Pheo",
              "Thyroidectomy <6 months"
            ],
            [
              "VHL",
              "VHL (3p25)",
              "Clear cell RCC, Hemangioblastoma, Pheo",
              "Bilateral RCC"
            ],
            [
              "Li-Fraumeni",
              "TP53",
              "Sarcoma, Breast, Brain, Leukemia",
              "Avoid radiation"
            ],
            [
              "Cowden",
              "PTEN (10q23)",
              "Breast, Follicular thyroid, Endometrial",
              "Trichilemmomas"
            ],
            [
              "Peutz-Jeghers",
              "STK11",
              "GI, Gynecologic, Breast, Pancreatic",
              "Lip pigmentation"
            ],
            [
              "HDGC",
              "CDH1",
              "Diffuse gastric, Lobular breast",
              "Prophylactic gastrectomy"
            ],
            [
              "Gorlin",
              "PTCH1 (9q22)",
              "BCC (multiple), Medulloblastoma",
              "Avoid radiation"
            ],
            [
              "NF1",
              "NF1 (17q11)",
              "MPNST, Glioma, Pheo",
              "Café-au-lait spots"
            ],
            [
              "MAP",
              "MUTYH",
              "CRC, Duodenal",
              "Autosomal RECESSIVE"
            ]
          ]
        }
      }
    ]
  },
  {
    "topic": "Adrenal",
    "color": "#1B5E20",
    "sections": [
      {
        "title": "Adrenal Incidentaloma — Biochemical Workup",
        "table": {
          "headers": [
            "Test",
            "Diagnoses",
            "Action if Positive"
          ],
          "rows": [
            [
              "1 mg overnight DST (cortisol >1.8 μg/dL = fail)",
              "Subclinical/overt Cushing's",
              "IPSS if ACTH-dependent; adrenalectomy if primary"
            ],
            [
              "Plasma metanephrines / 24-h urine catecholamines",
              "Pheochromocytoma",
              "Alpha-block → adrenalectomy"
            ],
            [
              "Aldosterone-to-renin ratio (ARR >30 + aldo >10)",
              "Primary hyperaldosteronism (Conn's)",
              "AVS → targeted adrenalectomy or spironolactone"
            ],
            [
              "DHEAS, 17-OH progesterone (if virilization)",
              "Adrenocortical carcinoma",
              "Adrenalectomy; mitotane adjuvant if high risk"
            ],
            [
              "CT HU unenhanced (>10 HU = indeterminate)",
              "Malignant/pheochromocytoma",
              "Functional workup before biopsy; >4 cm → resect"
            ]
          ]
        }
      },
      {
        "title": "Pheochromocytoma — Preoperative Management",
        "table": {
          "headers": [
            "Step",
            "Agent",
            "Duration / Goal"
          ],
          "rows": [
            [
              "1 — Alpha blockade",
              "Phenoxybenzamine 10 mg BID → titrate",
              "1–2 weeks preop; target BP <130/80"
            ],
            [
              "2 — Beta blockade (only AFTER alpha)",
              "Propranolol / atenolol",
              "For reflex tachycardia only; never start first"
            ],
            [
              "3 — Salt loading + hydration",
              "High-Na diet + IV fluid day of surgery",
              "Prevent profound hypotension post-resection"
            ],
            [
              "4 — Intraoperative crises",
              "Phentolamine / nitroprusside (HTN); NE (hypotension)",
              "Have ready at induction"
            ],
            [
              "5 — Post-op monitoring",
              "ICU 24 h; glucose, BP, electrolytes",
              "Hypoglycemia common from insulin rebound"
            ]
          ]
        }
      },
      {
        "title": "Adrenal Tumor Functional Syndromes",
        "table": {
          "headers": [
            "Tumor",
            "Hormone",
            "Classic Features",
            "Surgery?"
          ],
          "rows": [
            [
              "Pheochromocytoma",
              "Catecholamines",
              "Hypertensive crises, 5 H's (hypertension, headache, hyperhidrosis, hyperglycemia, heart palpitations)",
              "Yes — adrenalectomy after alpha block"
            ],
            [
              "Conn's adenoma",
              "Aldosterone",
              "HTN + hypokalemia + suppressed renin",
              "Yes (unilateral) — laparoscopic adrenalectomy"
            ],
            [
              "Cushing's adenoma",
              "Cortisol (ACTH-independent)",
              "Central obesity, striae, DM, osteoporosis, buffalo hump",
              "Yes — replace steroids periop"
            ],
            [
              "ACC",
              "Multiple hormones",
              "Mixed virilization/Cushing's, large mass, rapid growth",
              "Yes — open en-bloc; mitotane adjuvant"
            ],
            [
              "Non-functional",
              "None",
              "Incidentaloma — hormonal workup still required",
              "≥4 cm or growing → resect"
            ]
          ]
        }
      },
      {
        "title": "Rule of 10s — Pheochromocytoma",
        "table": {
          "headers": [
            "Rule",
            "Percentage",
            "Notes"
          ],
          "rows": [
            [
              "Bilateral",
              "10%",
              "Higher in MEN2, VHL, SDH mutations"
            ],
            [
              "Extra-adrenal",
              "10%",
              "Organ of Zuckerkandl most common; paraganglioma"
            ],
            [
              "Malignant",
              "10%",
              "No reliable histologic criteria; defined by metastasis"
            ],
            [
              "Pediatric",
              "10%",
              "More often bilateral, extra-adrenal, familial"
            ],
            [
              "Familial",
              "25–30%",
              "Screen all for RET, VHL, SDHB/D, MAX mutations"
            ]
          ]
        }
      }
    ]
  },
  {
    "topic": "Spleen",
    "color": "#4A148C",
    "sections": [
      {
        "title": "AAST Splenic Injury Grading",
        "table": {
          "headers": [
            "Grade",
            "CT/Operative Finding",
            "Management"
          ],
          "rows": [
            [
              "I",
              "Subcapsular hematoma <10%; laceration <1 cm deep",
              "NOM; observe"
            ],
            [
              "II",
              "Subcapsular 10–50%; laceration 1–3 cm; no trabecular vessel",
              "NOM; observe"
            ],
            [
              "III",
              "Subcapsular >50% or expanding; laceration >3 cm or trabecular vessel",
              "NOM + angioembolization if blush; OR if fails"
            ],
            [
              "IV",
              "Laceration involving segmental/hilar vessel; devascularization >25%",
              "Angioembolization or OR; splenectomy if unstable"
            ],
            [
              "V",
              "Completely shattered spleen; hilar vascular injury",
              "Emergency OR; splenectomy"
            ]
          ]
        }
      },
      {
        "title": "Post-Splenectomy Vaccination Schedule",
        "table": {
          "headers": [
            "Vaccine",
            "Timing (Elective)",
            "Timing (Emergency)",
            "Revaccination"
          ],
          "rows": [
            [
              "Pneumococcal (PCV20 or PCV15 + PPSV23)",
              "≥2 wk preop",
              "2 wk postop",
              "PPSV23 booster q5y"
            ],
            [
              "Meningococcal (MenACWY + MenB)",
              "≥2 wk preop",
              "2 wk postop",
              "MenACWY q5y"
            ],
            [
              "Haemophilus influenzae type b (Hib)",
              "≥2 wk preop",
              "2 wk postop",
              "Single dose (no revaccination)"
            ],
            [
              "Influenza",
              "Annual",
              "Annual",
              "Annual"
            ],
            [
              "COVID-19",
              "Per schedule",
              "Per schedule",
              "Per schedule"
            ]
          ]
        }
      },
      {
        "title": "Indications for Splenectomy",
        "table": {
          "headers": [
            "Condition",
            "Indication",
            "Considerations"
          ],
          "rows": [
            [
              "ITP",
              "Corticosteroid failure / chronic ITP",
              "2nd line after rituximab/TPO-RA; check for accessory spleen"
            ],
            [
              "Hereditary spherocytosis",
              "Symptomatic hemolytic anemia",
              "Delay until age ≥6 to preserve immune function; concurrent cholecystectomy if gallstones"
            ],
            [
              "Warm AIHA",
              "Steroid/rituximab failure",
              "Curative ~60%; check DAT before surgery"
            ],
            [
              "Hairy cell leukemia",
              "Massive splenomegaly / cytopenia",
              "Now 2nd-line after cladribine failure"
            ],
            [
              "Hypersplenism (portal HTN)",
              "Symptomatic cytopenias",
              "Consider PSE as alternative in cirrhosis"
            ],
            [
              "Splenic artery aneurysm",
              ">2 cm, symptomatic, or any size in pregnancy",
              "Endovascular or open; laparoscopic splenectomy with SAA"
            ],
            [
              "Trauma",
              "Hemodynamic instability / failed NOM",
              "Attempt damage control / splenorrhaphy if feasible"
            ]
          ]
        }
      },
      {
        "title": "OPSI — Overwhelming Post-Splenectomy Infection",
        "table": {
          "headers": [
            "Feature",
            "Details"
          ],
          "rows": [
            [
              "Organisms",
              "S. pneumoniae (50–90%), H. influenzae, N. meningitidis; also Capnocytophaga (dog bites), Babesia, malaria"
            ],
            [
              "Risk period",
              "Highest in first 2 years; lifelong elevated risk"
            ],
            [
              "Presentation",
              "Flu-like prodrome → fulminant sepsis within 24 h; DIC, adrenal insufficiency (Waterhouse-Friderichsen)"
            ],
            [
              "Mortality",
              "50–70% once established"
            ],
            [
              "Prevention",
              "Vaccination + prophylactic penicillin V 250 mg BID (at least 2 yrs; lifelong in children)"
            ],
            [
              "Emergency plan",
              "Patient carries antibiotics (amoxicillin 3 g stat); medic-alert bracelet"
            ]
          ]
        }
      }
    ]
  },
  {
    "topic": "Liver",
    "color": "#E65100",
    "sections": [
      {
        "title": "Child-Pugh Score",
        "table": {
          "headers": [
            "Parameter",
            "1 Point",
            "2 Points",
            "3 Points"
          ],
          "rows": [
            [
              "Bilirubin (μmol/L)",
              "<34",
              "34–50",
              ">50"
            ],
            [
              "Albumin (g/L)",
              ">35",
              "28–35",
              "<28"
            ],
            [
              "INR",
              "<1.7",
              "1.7–2.3",
              ">2.3"
            ],
            [
              "Ascites",
              "None",
              "Mild (diuretic-responsive)",
              "Moderate–severe (refractory)"
            ],
            [
              "Encephalopathy",
              "None",
              "Grade 1–2",
              "Grade 3–4"
            ],
            [
              "Class",
              "A (5–6): resectable",
              "B (7–9): borderline",
              "C (10–15): transplant only"
            ]
          ]
        }
      },
      {
        "title": "Hepatic Benign Tumors — Differentiation",
        "table": {
          "headers": [
            "Feature",
            "Hemangioma",
            "FNH",
            "Hepatic Adenoma"
          ],
          "rows": [
            [
              "Background",
              "Most common benign liver tumor",
              "Hyperplastic response to anomalous artery",
              "OCP/anabolic steroid use"
            ],
            [
              "Imaging",
              "Peripheral nodular enhancement; MRI T2 bright",
              "Central scar; spoke-wheel vessels; Tc-99m uptake",
              "No central scar; arterial enhancement"
            ],
            [
              "Malignant potential",
              "None",
              "None",
              "Yes (~5–8% if >5 cm)"
            ],
            [
              "Rupture risk",
              "Very low",
              "Very low",
              "10–25% (higher in men, pregnancy)"
            ],
            [
              "Treatment",
              "Observe; resect only if symptomatic/large",
              "Observe (stop OCPs not needed)",
              "Stop OCPs; resect if >5 cm or growing"
            ]
          ]
        }
      },
      {
        "title": "HCC — Milan vs UCSF Criteria for Transplant",
        "table": {
          "headers": [
            "Criteria",
            "Tumor Size/Number",
            "5-yr Survival Post-Tx"
          ],
          "rows": [
            [
              "Milan",
              "Single ≤5 cm OR ≤3 nodules each ≤3 cm; no vascular invasion; no extrahepatic disease",
              "~70%"
            ],
            [
              "UCSF (expanded)",
              "Single ≤6.5 cm OR ≤3 nodules (largest ≤4.5 cm, total ≤8 cm)",
              "~60%"
            ],
            [
              "Beyond Milan/UCSF",
              "Downstaging with TACE/TARE may qualify for transplant",
              "Variable by response"
            ]
          ]
        }
      },
      {
        "title": "Liver Resection — Key Anatomy",
        "table": {
          "headers": [
            "Landmark",
            "Definition",
            "Clinical Use"
          ],
          "rows": [
            [
              "Cantlie's line (Rex-Cantlie)",
              "Gallbladder fossa → IVC; divides right and left hemilivers",
              "Plane of right/left hepatectomy"
            ],
            [
              "Couinaud segments",
              "8 segments based on hepatic veins + portal pedicles",
              "Describes resection volume precisely"
            ],
            [
              "Segment I (caudate)",
              "Separate portal supply; drains directly to IVC via short veins",
              "Involved in Budd-Chiari; must identify short veins"
            ],
            [
              "Future liver remnant (FLR)",
              "Normal liver: ≥20–25%; cirrhosis: ≥40%; chemo-damaged: ≥30%",
              "Portal vein embolization to hypertrophy FLR"
            ],
            [
              "Pringle maneuver",
              "Clamp hepatoduodenal ligament (portal vein + hepatic artery)",
              "Safe ischemia: 60 min normal, 30 min cirrhotic"
            ]
          ]
        }
      },
      {
        "title": "Portal Hypertension — Treatment Ladder",
        "table": {
          "headers": [
            "Intervention",
            "Indication",
            "Notes"
          ],
          "rows": [
            [
              "Non-selective beta-blocker (propranolol/carvedilol)",
              "Primary prophylaxis (varices)",
              "Reduce portal pressure; avoid in SBP/refractory ascites"
            ],
            [
              "EVL (endoscopic variceal ligation)",
              "Primary prophylaxis (large varices) OR acute bleeding",
              "Obliterates varices; 2–4 sessions"
            ],
            [
              "Octreotide (terlipressin) + EVL",
              "Acute variceal bleeding",
              "First 48–72h; reduces portal pressure 20–25%"
            ],
            [
              "TIPS",
              "Refractory bleeding, refractory ascites, Budd-Chiari",
              "Encephalopathy risk; contraindicated in severe HE, heart failure"
            ],
            [
              "Liver transplant",
              "End-stage liver disease, Child C, MELD >15",
              "Definitive; treats underlying cause"
            ]
          ]
        }
      }
    ]
  },
  {
    "topic": "Pancreas",
    "color": "#B71C1C",
    "sections": [
      {
        "title": "Ranson Criteria for Acute Pancreatitis",
        "table": {
          "headers": [
            "On Admission",
            "At 48 Hours",
            "Score / Mortality"
          ],
          "rows": [
            [
              "Age >55",
              "Ca2+ <8 mg/dL",
              "0–2: <1% mortality"
            ],
            [
              "WBC >16,000",
              "BUN rise >5 mg/dL",
              "3–4: 15% mortality"
            ],
            [
              "Glucose >200 mg/dL",
              "PaO2 <60 mmHg",
              "5–6: ~40% mortality"
            ],
            [
              "LDH >350 IU/L",
              "Base deficit >4 mEq/L",
              "≥7: ~100% mortality"
            ],
            [
              "AST >250 IU/L",
              "Fluid sequestration >6 L",
              "BISAP, APACHE-II also used"
            ]
          ]
        }
      },
      {
        "title": "Pancreatic Cystic Neoplasms — Key Differences",
        "table": {
          "headers": [
            "Feature",
            "Serous Cystadenoma",
            "Mucinous Cystic Neoplasm (MCN)",
            "IPMN (Branch-duct)",
            "Pseudocyst"
          ],
          "rows": [
            [
              "Patient",
              "Older women",
              "Middle-aged women",
              "Older adults (M=F for MD-IPMN)",
              "Any; hx pancreatitis"
            ],
            [
              "Location",
              "Body/tail",
              "Body/tail",
              "Head (branch-duct); any (MD)",
              "Any"
            ],
            [
              "Imaging",
              "Honeycomb; central scar ± calcification",
              "Macrocysts; no duct communication; ovarian stroma",
              "Communicates with MPD",
              "Unilocular; no septa"
            ],
            [
              "CEA (cyst fluid)",
              "Low (<5)",
              "High (>192)",
              "Variable (high if malignant)",
              "Low"
            ],
            [
              "Malignancy risk",
              "<1% (benign)",
              "~10–17%",
              "MD-IPMN ~45–60%; BD ~1–3%",
              "None (pseudocyst)"
            ],
            [
              "Management",
              "Observe",
              "Resect all surgical candidates",
              "Per Fukuoka guidelines",
              "Drain if symptomatic (EUS-guided)"
            ]
          ]
        }
      },
      {
        "title": "Functional Pancreatic Endocrine Tumors",
        "table": {
          "headers": [
            "Tumor",
            "Hormone",
            "Syndrome",
            "Key Feature",
            "Treatment"
          ],
          "rows": [
            [
              "Insulinoma",
              "Insulin",
              "Whipple's triad (hypoglycemia + symptoms + relief with glucose)",
              "90% benign, 90% solitary",
              "Enucleation or distal pancreatectomy"
            ],
            [
              "Gastrinoma (ZES)",
              "Gastrin",
              "Peptic ulcers, diarrhea; secretin → paradoxical ↑ gastrin",
              "MEN1 in 25%; gastrinoma triangle",
              "PPI; sporadic → resect; MEN1 → medical"
            ],
            [
              "VIPoma",
              "VIP",
              "WDHA (watery diarrhea, hypokalemia, achlorhydria)",
              "Often tail; >50% metastatic",
              "Resect; octreotide preop"
            ],
            [
              "Glucagonoma",
              "Glucagon",
              "4 D's: Dermatitis (NME), Diabetes, DVT, Depression",
              "Tail; large at diagnosis",
              "Resect + octreotide + anticoagulate"
            ],
            [
              "Somatostatinoma",
              "Somatostatin",
              "Diabetes + cholelithiasis + steatorrhea",
              "Rare; periampullary",
              "Resect if resectable"
            ]
          ]
        }
      },
      {
        "title": "Whipple (Pancreaticoduodenectomy) — Key Points",
        "table": {
          "headers": [
            "Aspect",
            "Details"
          ],
          "rows": [
            [
              "Resection",
              "Head, uncinate, duodenum, 1st 15 cm jejunum, gallbladder, distal CBD, distal stomach (classic) or pylorus-preserving"
            ],
            [
              "Reconstruction order",
              "Pancreaticojejunostomy → hepaticojejunostomy → gastrojejunostomy (all to same Roux limb)"
            ],
            [
              "Critical vessel",
              "Identify and preserve SMA (medial dissection last); ligate GDA; aberrant RHA in 15–20%"
            ],
            [
              "POPF risk",
              "Soft texture + small duct (<3 mm) → highest fistula risk; drain amylase >3× serum on POD3 = fistula"
            ],
            [
              "DGE (delayed gastric emptying)",
              "Most common complication (~20%); NG decompression; prokinetics"
            ],
            [
              "PPPD benefit",
              "Preserves pylorus → less dumping, similar oncologic outcome to classic Whipple"
            ]
          ]
        }
      },
      {
        "title": "Chronic Pancreatitis — Surgical Options",
        "table": {
          "headers": [
            "Procedure",
            "Indication",
            "Notes"
          ],
          "rows": [
            [
              "Puestow / Partington-Rochelle (lateral PJ)",
              "Large duct (MPD ≥7 mm) + chronic pain",
              "Longitudinal incision of MPD → Roux-en-Y; ~75% pain relief"
            ],
            [
              "Beger procedure",
              "Dominant head mass (duodenum-preserving)",
              "Resect head, preserve duodenum; good for inflammatory head mass"
            ],
            [
              "Frey procedure (LPJ + head coring)",
              "Large duct + head mass",
              "Combines Beger + Puestow; most widely used"
            ],
            [
              "Distal pancreatectomy",
              "Disease limited to tail",
              "If left-sided dominant disease"
            ],
            [
              "TPIAT (total pancreatectomy + islet autotransplant)",
              "Hereditary/small-duct pancreatitis; failed prior operations",
              "Prevents surgical diabetes; specialized centers only"
            ]
          ]
        }
      }
    ]
  },
  {
    "topic": "Trauma",
    "color": "#B71C1C",
    "sections": [
      {
        "title": "Primary Survey — ABCDE",
        "table": {
          "headers": [
            "Step",
            "Action",
            "Key Threat"
          ],
          "rows": [
            [
              "A — Airway (C-spine)",
              "Jaw thrust, chin lift; intubate if GCS ≤8 or unable to protect airway",
              "Obstruction, vomiting"
            ],
            [
              "B — Breathing",
              "Inspect, percuss, auscultate; decompress tension PTX",
              "Tension PTX, hemothorax, open PTX, flail chest"
            ],
            [
              "C — Circulation",
              "2 large IVs; FAST; control external bleeding (tourniquet, direct pressure)",
              "Hemorrhagic shock; cardiac tamponade"
            ],
            [
              "D — Disability",
              "GCS, pupils, motor; glucose",
              "Herniation, herniation signs, hypoglycemia"
            ],
            [
              "E — Exposure / Environment",
              "Undress, logroll, foley, NG tube; keep warm",
              "Missed injuries, hypothermia"
            ]
          ]
        }
      },
      {
        "title": "Hemorrhagic Shock Classification",
        "table": {
          "headers": [
            "Class",
            "Blood Loss (mL)",
            "% Volume",
            "HR",
            "BP",
            "RR",
            "Mental Status",
            "Treatment"
          ],
          "rows": [
            [
              "I",
              "≤750",
              "≤15%",
              "<100",
              "Normal",
              "14–20",
              "Normal/anxious",
              "Crystalloid"
            ],
            [
              "II",
              "750–1500",
              "15–30%",
              "100–120",
              "Normal",
              "20–30",
              "Anxious",
              "Crystalloid + blood"
            ],
            [
              "III",
              "1500–2000",
              "30–40%",
              "120–140",
              "↓",
              "30–40",
              "Confused",
              "Blood products"
            ],
            [
              "IV",
              ">2000",
              ">40%",
              ">140",
              "Very low",
              "<35",
              "Lethargic/unconscious",
              "Massive transfusion + OR"
            ]
          ]
        }
      },
      {
        "title": "Retroperitoneal Hematoma — Zone Management",
        "table": {
          "headers": [
            "Zone",
            "Location",
            "Blunt Trauma",
            "Penetrating Trauma"
          ],
          "rows": [
            [
              "Zone 1 (central)",
              "Midline: aorta, IVC, SMA, celiac",
              "Always explore",
              "Always explore"
            ],
            [
              "Zone 2 (flank)",
              "Lateral: renal vessels, kidney",
              "Non-expanding: observe; expanding: explore",
              "Always explore"
            ],
            [
              "Zone 3 (pelvic)",
              "Pelvic vessels, iliac",
              "Do NOT explore (packing + pelvic binder + angioembolization)",
              "Explore (uncontrolled pelvic hemorrhage)"
            ]
          ]
        }
      },
      {
        "title": "Damage Control Surgery (DCS) — Indications & Steps",
        "table": {
          "headers": [
            "DCS Stage",
            "Action",
            "Indication"
          ],
          "rows": [
            [
              "Stage 0 — pre-hospital",
              "Permissive hypotension; minimal crystalloid; tourniquets; airway",
              "SBP 80–90 mmHg target until hemorrhage control"
            ],
            [
              "Stage 1 — OR",
              "Hemorrhage control (packing, ligation, shunts); contamination control (staple bowel); TAC",
              "pH <7.2; Temp <35°C; INR >1.5; no time for anastomosis"
            ],
            [
              "Stage 2 — ICU",
              "Correct lethal triad; 1:1:1 MTP; warm; vasopressors",
              "Continue resuscitation 24–48 h"
            ],
            [
              "Stage 3 — re-look OR",
              "Definitive repair; anastomosis; closure",
              "When physiology normalized"
            ],
            [
              "TAC options",
              "Bogota bag, KCI Prevena, Wittmann patch",
              "Open abdomen management; planned closure"
            ]
          ]
        }
      },
      {
        "title": "Massive Transfusion Protocol (MTP)",
        "table": {
          "headers": [
            "Product",
            "Ratio",
            "Target",
            "Notes"
          ],
          "rows": [
            [
              "PRBCs : FFP : Platelets",
              "1 : 1 : 1",
              "Hgb >7–8; INR <1.5; Plt >50K",
              "PROPPR trial: 1:1:1 = improved hemostasis + survival"
            ],
            [
              "Cryoprecipitate",
              "Every 2 packs PRBCs",
              "Fibrinogen >200 mg/dL",
              "Contains fibrinogen, factor VIII, vWF, XIII"
            ],
            [
              "TXA (tranexamic acid)",
              "1 g IV over 10 min, then 1 g over 8 h",
              "Give within 3 h of injury",
              "CRASH-2 trial; anti-fibrinolytic; reduces mortality"
            ],
            [
              "Calcium (CaCl2 or gluconate)",
              "1 g per 4 units PRBCs",
              "iCa >1.1 mmol/L",
              "Citrate in stored blood chelates calcium → hypocalcemia → poor coagulation"
            ],
            [
              "Permissive hypotension",
              "SBP 80–90 (blunt); 60–70 (penetrating)",
              "Until surgical hemorrhage control",
              "Avoid in TBI (maintain CPP); avoid in elderly"
            ]
          ]
        }
      }
    ]
  },
  {
    "topic": "General Surgery",
    "color": "#1A237E",
    "sections": [
      {
        "title": "Fluid Resuscitation — Types & Indications",
        "table": {
          "headers": [
            "Fluid",
            "Composition",
            "Indication",
            "Avoid"
          ],
          "rows": [
            [
              "0.9% Normal Saline",
              "154 mEq/L Na, 154 mEq/L Cl",
              "Hypochloremic metabolic alkalosis; neurosurgical pt; hyponatremia",
              "Large volumes → hyperchloremic acidosis; renal failure (↑K)"
            ],
            [
              "Lactated Ringer's (LR)",
              "130 Na, 4 K, 109 Cl, 28 lactate, 3 Ca",
              "Hemorrhagic shock resuscitation; burns; periop",
              "Hyponatremia; hepatic failure (lactate metabolism)"
            ],
            [
              "Plasmalyte",
              "140 Na, 5 K, 98 Cl, 27 gluconate, 23 acetate",
              "Balanced alternative to NS and LR",
              "More expensive; less studied"
            ],
            [
              "D5W",
              "Free water + 50 g/L glucose",
              "Maintenance; hypernatremia correction",
              "Never for resuscitation; hyponatremia risk"
            ],
            [
              "Albumin 5%",
              "Oncotic agent",
              "Spontaneous bacterial peritonitis; paracentesis >5L; hepatorenal syndrome",
              "Not for acute resuscitation"
            ]
          ]
        }
      },
      {
        "title": "Surgical Wound Classification & SSI Risk",
        "table": {
          "headers": [
            "Class",
            "Definition",
            "Examples",
            "Prophylaxis Duration"
          ],
          "rows": [
            [
              "Clean (I)",
              "Non-contaminated; no GI/GU/respiratory entry",
              "Hernia, thyroid, mastectomy",
              "Single preop dose; no continued abx"
            ],
            [
              "Clean-contaminated (II)",
              "Controlled entry to GI/GU/respiratory tract",
              "Bowel resection, appendectomy (not perforated), cholecystectomy",
              "Single preop dose"
            ],
            [
              "Contaminated (III)",
              "Gross spillage; non-purulent inflammation; open/fresh traumatic wound",
              "Perforated diverticulitis, open fracture",
              "24 h postop"
            ],
            [
              "Dirty/infected (IV)",
              "Pus, perforated viscus, old traumatic wound with necrosis",
              "Feculent peritonitis, necrotizing fasciitis",
              "Therapeutic (7–10 days)"
            ]
          ]
        }
      },
      {
        "title": "Anastomotic Leak — Diagnosis & Management",
        "table": {
          "headers": [
            "Aspect",
            "Details"
          ],
          "rows": [
            [
              "Timing",
              "Most common POD 4–7 (colonic); POD 3–5 (small bowel)"
            ],
            [
              "Clinical signs",
              "Fever, tachycardia, abdominal pain, drain amylase/bile, feculent drain output"
            ],
            [
              "Diagnosis",
              "CT scan with oral/rectal contrast; water-soluble contrast enema"
            ],
            [
              "Contained/small leak",
              "NPO + IV antibiotics + drain (percutaneous if not already draining)"
            ],
            [
              "Uncontained/peritonitis",
              "OR: washout ± diversion (Hartmann's or loop ostomy) ± repair/resection"
            ],
            [
              "Risk factors",
              "Tension, ischemia, poor nutrition (albumin <3), radiation, steroids, bowel prep inadequacy, Hgb <7"
            ]
          ]
        }
      },
      {
        "title": "Postoperative Complications — Classic Timeline",
        "table": {
          "headers": [
            "Postop Day",
            "Complication",
            "Cause"
          ],
          "rows": [
            [
              "0–1",
              "Hemorrhage, respiratory (atelectasis)",
              "Inadequate hemostasis; splinting from pain"
            ],
            [
              "1–3",
              "Fever: Wind (atelectasis/pneumonia), Water (UTI), Wound (SSI early)",
              "Pulmonary toilet; adequate analgesia"
            ],
            [
              "3–5",
              "Anastomotic leak (small bowel); DVT begins",
              "Technical; ischemia"
            ],
            [
              "4–7",
              "Anastomotic leak (colon); SSI peaks",
              "Bacterial contamination; tissue breakdown"
            ],
            [
              "5–7",
              "Intra-abdominal abscess",
              "Residual contamination"
            ],
            [
              ">7",
              "Pulmonary embolism; ostomy complications",
              "Hypercoagulability; stoma ischemia/retraction"
            ]
          ]
        }
      }
    ]
  },
  {
    "topic": "Critical Care",
    "color": "#880E4F",
    "sections": [
      {
        "title": "Sepsis-3 Definitions",
        "table": {
          "headers": [
            "Definition",
            "Criteria",
            "Notes"
          ],
          "rows": [
            [
              "SIRS (not Sepsis-3)",
              "≥2: Temp >38 or <36°C; HR >90; RR >20 or PaCO2 <32; WBC >12K, <4K, or >10% bands",
              "Retired as sepsis definition; too non-specific"
            ],
            [
              "Sepsis",
              "Life-threatening organ dysfunction caused by dysregulated host response to infection; SOFA score ≥2 (acute change)",
              "New organ dysfunction + suspected infection"
            ],
            [
              "Septic Shock",
              "Sepsis + vasopressor required to maintain MAP ≥65 + lactate >2 mmol/L despite adequate fluid resuscitation",
              "Mortality ~40%"
            ],
            [
              "qSOFA (screening)",
              "≥2 of: altered mental status, RR ≥22, SBP ≤100",
              "Rapid bedside screen; not for ICU (use SOFA)"
            ]
          ]
        }
      },
      {
        "title": "SOFA Score (Sequential Organ Failure Assessment)",
        "table": {
          "headers": [
            "Organ",
            "Parameter",
            "Score 1",
            "Score 2",
            "Score 3",
            "Score 4"
          ],
          "rows": [
            [
              "Respiratory",
              "PaO2/FiO2 (mmHg)",
              "<400",
              "<300",
              "<200 (ventilated)",
              "<100 (ventilated)"
            ],
            [
              "Coagulation",
              "Platelets (×10³/μL)",
              "<150",
              "<100",
              "<50",
              "<20"
            ],
            [
              "Liver",
              "Bilirubin (μmol/L)",
              "20–32",
              "33–101",
              "102–203",
              ">204"
            ],
            [
              "Cardiovascular",
              "MAP/vasopressors",
              "MAP <70",
              "Dopa ≤5 or Dobu",
              "Dopa 5–15 or epi/norepi ≤0.1",
              "Dopa >15 or epi/norepi >0.1"
            ],
            [
              "CNS",
              "GCS",
              "13–14",
              "10–12",
              "6–9",
              "<6"
            ],
            [
              "Renal",
              "Creatinine (μmol/L) / urine output",
              "110–170",
              "171–299",
              "300–440 or <500 mL/day",
              ">440 or <200 mL/day"
            ]
          ]
        }
      },
      {
        "title": "Vasopressors & Inotropes — Mechanisms & Dosing",
        "table": {
          "headers": [
            "Drug",
            "Receptors",
            "Dose",
            "Primary Use",
            "Key Notes"
          ],
          "rows": [
            [
              "Norepinephrine (NE)",
              "α1 >> β1",
              "0.01–3 μg/kg/min",
              "First-line septic shock",
              "Increases SVR + MAP; minimal HR effect; first-line per Surviving Sepsis Campaign"
            ],
            [
              "Vasopressin",
              "V1 (vascular)",
              "0.03–0.04 units/min (fixed dose)",
              "Add-on to NE in refractory shock",
              "Does not increase cardiac output; reduces NE dose; mesenteric ischemia risk"
            ],
            [
              "Epinephrine",
              "β1=β2 > α1",
              "0.01–1 μg/kg/min",
              "Anaphylaxis, cardiac arrest, vasodilatory shock",
              "Increases CO and SVR; significant metabolic effects (↑lactate, ↑glucose)"
            ],
            [
              "Dopamine",
              "Dose-dependent: DA → β1 → α1",
              "1–20 μg/kg/min",
              "Alternative to NE (less preferred)",
              "Arrhythmogenic; 'renal dose' dopamine is a myth; associated with higher mortality than NE"
            ],
            [
              "Dobutamine",
              "β1 > β2",
              "2–20 μg/kg/min",
              "Cardiogenic shock; low CO states",
              "Positive inotrope; reduces preload/afterload; may cause hypotension + tachycardia"
            ],
            [
              "Phenylephrine",
              "Pure α1",
              "100–400 μg/min",
              "Neurogenic shock; anesthesia-induced hypotension",
              "Pure vasoconstrictor; reflex bradycardia; avoid in cardiogenic shock"
            ]
          ]
        }
      },
      {
        "title": "Mechanical Ventilation — Key Settings & ARDS",
        "table": {
          "headers": [
            "Parameter",
            "Setting",
            "Rationale"
          ],
          "rows": [
            [
              "Tidal volume (VT)",
              "6 mL/kg IBW (lung-protective)",
              "ARDSNet: reduces barotrauma; mortality benefit"
            ],
            [
              "Plateau pressure (Pplat)",
              "<30 cm H2O",
              "Marker of alveolar overdistension; correlates with lung injury"
            ],
            [
              "Driving pressure",
              "<15 cm H2O (Pplat − PEEP)",
              "Strongest predictor of ARDS mortality"
            ],
            [
              "PEEP",
              "5–18 cm H2O (titrate per ARDSnet or FiO2)",
              "Recruits alveoli; prevents derecruitment; improves oxygenation"
            ],
            [
              "FiO2",
              "Titrate to SpO2 88–95%",
              "Minimize O2 toxicity; accept permissive hypoxemia"
            ],
            [
              "ARDS Berlin Definition",
              "Mild: PF 200–300; Moderate: 100–200; Severe: <100 on PEEP ≥5",
              "Bilateral infiltrates; acute onset ≤7 days; not fully cardiac"
            ]
          ]
        }
      },
      {
        "title": "ICU Nutrition Guidelines",
        "table": {
          "headers": [
            "Parameter",
            "Recommendation",
            "Notes"
          ],
          "rows": [
            [
              "Timing",
              "Start EN within 24–48h of ICU admission if hemodynamically stable",
              "Early EN preserves gut barrier; reduces infections"
            ],
            [
              "Route",
              "Enteral > parenteral",
              "EN maintains gut immunity; PN only if EN contraindicated/not tolerated for >7 days"
            ],
            [
              "Caloric goal",
              "25 kcal/kg/day (trophic 10–20 kcal/kg in first week)",
              "Avoid overfeeding; trophic feeds acceptable early"
            ],
            [
              "Protein",
              "1.2–2 g/kg/day",
              "Higher in burns, trauma, CRRT (2–2.5 g/kg/day)"
            ],
            [
              "Glycemic control",
              "Insulin infusion: target BG 140–180 mg/dL",
              "NICE-SUGAR: tight control (81–108) → ↑ mortality from hypoglycemia"
            ],
            [
              "TPN indication",
              "GI failure; unable to meet >60% of needs via EN by day 7",
              "Peripheral PN (PPN) for short-term; central PN for >10–14 days"
            ]
          ]
        }
      },
      {
        "title": "Common ICU Electrolyte Disorders",
        "table": {
          "headers": [
            "Disorder",
            "Cause (Surgical)",
            "Treatment",
            "Notes"
          ],
          "rows": [
            [
              "Hyponatremia",
              "SIADH (pain, narcotics); over-hypotonic fluid; adrenal insufficiency",
              "Fluid restriction; 3% NaCl if symptomatic; correct ≤10 mEq/day",
              "Rapid correction → central pontine myelinolysis"
            ],
            [
              "Hypernatremia",
              "Inadequate free water; diabetes insipidus (post-cranial surgery); nasogastric output",
              "Free water via NG; D5W IV; desmopressin for DI",
              "Correct slowly ≤10 mEq/day"
            ],
            [
              "Hypokalemia",
              "GI losses (vomiting, NG, diarrhea, ileus); diuretics; alkalosis",
              "IV KCl (central for >20 mEq/h); 40 mEq/L PO",
              "Causes arrhythmias; correct Mg first"
            ],
            [
              "Hyperkalemia",
              ">6.5: ESRD; crush injury; hemolysis; K-sparing diuretics",
              "Ca gluconate (membrane stabilization) → insulin/glucose → kayexalate/dialysis",
              "ECG changes (peaked T, wide QRS) guide urgency"
            ],
            [
              "Hypomagnesemia",
              "NG suction; TPN without Mg; alcoholism; loop diuretics",
              "Mg sulfate 1–2 g IV over 1h",
              "Required for K+ repletion; prolonged QT; seizures"
            ],
            [
              "Hypophosphatemia",
              "Refeeding syndrome; TPN; alkalosis; antacids",
              "PO phosphate (mild); IV sodium/potassium phosphate (severe)",
              "Refeeding: start TPN/EN slowly; give thiamine first"
            ]
          ]
        }
      },
      {
        "title": "Acute Kidney Injury (AKI) — KDIGO Staging",
        "table": {
          "headers": [
            "Stage",
            "Creatinine Criteria",
            "Urine Output",
            "Management"
          ],
          "rows": [
            [
              "Stage 1",
              "↑ Cr ≥0.3 mg/dL within 48h OR ≥1.5–1.9× baseline",
              "<0.5 mL/kg/h for 6–12h",
              "Remove nephrotoxins; optimize volume; avoid contrast"
            ],
            [
              "Stage 2",
              "Cr 2.0–2.9× baseline",
              "<0.5 mL/kg/h for ≥12h",
              "Same + monitor closely; avoid NSAIDS/ACEi/diuretics if oliguric"
            ],
            [
              "Stage 3",
              "Cr ≥3× baseline OR ≥4.0 mg/dL OR RRT initiated",
              "<0.3 mL/kg/h for ≥24h OR anuria ≥12h",
              "Consider RRT (CRRT preferred in hemodynamically unstable)"
            ],
            [
              "RRT indications",
              "A-E-I-O-U: Acidosis (pH <7.1), Electrolyte (K >6.5), Intoxication, Overload (fluid-refractory), Uremia (encephalopathy/pericarditis)",
              "—",
              "Intermittent HD vs CRRT based on hemodynamics"
            ]
          ]
        }
      },
      {
        "title": "Abdominal Compartment Syndrome (ACS)",
        "table": {
          "headers": [
            "Parameter",
            "Normal",
            "Grade I",
            "Grade II",
            "Grade III",
            "Grade IV"
          ],
          "rows": [
            [
              "IAP (mmHg)",
              "<12",
              "12–15",
              "16–20",
              "21–25",
              ">25"
            ],
            [
              "Organ effects",
              "None",
              "Mild↑ peak airway P",
              "Oliguria, ↑ ventilator P",
              "Anuria, respiratory failure",
              "Multi-organ failure"
            ],
            [
              "Management",
              "—",
              "Conservative measures",
              "Optimize volume; consider decompression",
              "Decompressive laparotomy",
              "Emergency decompressive laparotomy"
            ]
          ]
        }
      },
      {
        "title": "Ventilator-Associated Events (VAP/VAE) — Prevention Bundle",
        "table": {
          "headers": [
            "Intervention",
            "Frequency",
            "Benefit"
          ],
          "rows": [
            [
              "HOB elevation 30–45°",
              "Continuous",
              "Reduces aspiration; VAP risk ↓"
            ],
            [
              "Oral care (chlorhexidine)",
              "Q4–12h",
              "Reduces oropharyngeal colonization"
            ],
            [
              "Spontaneous awakening trials (SAT)",
              "Daily",
              "Paired with SBT reduces ICU LOS + mortality"
            ],
            [
              "Spontaneous breathing trials (SBT)",
              "Daily (if passes SAT)",
              "Earliest safe extubation"
            ],
            [
              "VTE prophylaxis",
              "Daily (heparin or LMWH)",
              "CLOT prevention in ICU patients"
            ],
            [
              "Stress ulcer prophylaxis",
              "PPIs or H2 blockers",
              "Indicated: coagulopathy, mechanical ventilation >48h"
            ]
          ]
        }
      }
    ]
  }
]

import importlib.util as _ilu, sys as _sys
if __name__ == "__main__":
    import subprocess, sys
    subprocess.run([sys.executable,
        "/sessions/jolly-sweet-galileo/mnt/outputs/restyle_app.py"])
