import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
import random as r

form_class = uic.loadUiType("test 6.ui")[0]


E = ['tenant', 'thrust', 'unanimous', 'validate', 'tyrant', 'confirm', 'constrain', 'preliminary', 'stance', 'velocity', 'nomadic', 'deform', 'superstitious', 'cogent', 'conscientious', 'override', 'perspiration', 'precede', 'attribute', 'deliberate',
         'obstruct', 'flammable', 'testify', 'lease', 'proclaim', 'impoverish', 'cumulative', 'enforce', 'contradict', 'interrupt', 'augment', 'prestige', 'behold', 'applicable', 'proactive', 'compelling', 'extravagant', 'cognitive', 'tact', 'expel',
         'truce', 'reconcile', 'supreme', 'inexhaustible', 'summon', 'poise', 'stifle', 'omission', 'tactic', 'aboriginal', 'indignant', 'prioritize', 'desert', 'deceptive', 'sojourn', 'brag', 'grievous', 'impatience', 'snore', 'hospitality',
         'captive', 'condense', 'elicit', 'nutritious', 'quiver', 'evacuate', 'electoral', 'authoritarian', 'dreadful', 'disdain', 'sentiment', 'causal', 'seductive', 'relish', 'indigenous', 'condemn', 'dictator', 'extinguish', 'criterion', 'throne',
         'convince', 'freight', 'imperative', 'resourceful', 'ingratitude', 'revolve', 'shabby', 'certify', 'assert', 'disillusion', 'comprehensive', 'inhale', 'segregate', 'excavate', 'sewage', 'marital', 'tilt', 'deploy', 'intimidate', 'disjoin',
         'contend', 'inverse', 'catalyst', 'altruistic', 'posture', 'intact', 'immerse', 'traverse', 'pious', 'savor', 'verse', 'strangle', 'hostage', 'rash', 'pledge', 'inconsistent', 'traitor', 'unfounded', 'connotation', 'marginalize',
         'legislature', 'retort', 'plead', 'grim', 'overwhelm', 'frail', 'subside', 'perseverance', 'artisan', 'adhesive', 'acquaint', 'renovate', 'satiate', 'proposition', 'congest', 'disprove', 'neutralize', 'segment', 'masculine', 'recurrent',
         'ponder', 'impenetrable', 'pregnant', 'serenity', 'hypothesize', 'instill', 'despise', 'eradicate', 'venue', 'scant', 'jury', 'compound', 'indiscriminate', 'subdue', 'confide', 'emphatic', 'sibling', 'incidence', 'modification', 'polarize',
         'impartial', 'attune', 'ignorant', 'involuntary', 'inflict', 'pretense', 'perpetuate', 'hygienic', 'populate', 'ascend', 'equity', 'sarcastic', 'shiver', 'devastate', 'casualty', 'refer', 'detract', 'temperate', 'punctuate', 'senate',
         'stubborn', 'mischievous', 'absurdity', 'entrench', 'snob', 'cohesive', 'prudence', 'demanding', 'autonomous', 'precept', 'shudder', 'tenure', 'sanitation', 'ingenious', 'tread', 'itinerary', 'courteous', 'divert', 'convict', 'disruption',
         'fluctuate', 'slaughter', 'obsession', 'allure', 'dehydrate', 'instigate', 'coward', 'vocation', 'compassionate', 'trivial', 'rustic', 'exhort', 'aviation', 'anonymity', 'inflexible', 'versatile', 'conductive', 'sermon', 'spoilage', 'yearn',
         'triumphant', 'monk', 'fragrance', 'monopoly', 'decompose', 'inaccessible', 'prevention', 'mundane', 'hypocritical', 'obese', 'compulsory', 'duplicate', 'refrain', 'detached', 'funeral', 'cliche', 'repent', 'efficacy', 'layman', 'prolong',
         'empathize', 'plantation', 'gnaw', 'temper', 'transcend', 'obstinate', 'stingy', 'lurk', 'elated', 'sober', 'implore', 'conquest', 'irreversible', 'ample', 'underlying', 'analogous', 'discrepancy', 'inadequate', 'justification', 'slack',
         'conclusive', 'dispense', 'plunder', 'rebel', 'coincide', 'crumble', 'deplete', 'catastrophe', 'torture', 'mutate', 'tangle', 'reunify', 'transparent', 'germinate', 'mortgage', 'inquisitive', 'reproach', 'obsolete', 'riot', 'nominal',
         'betrayal', 'publicize', 'sniff', 'splendid', 'unorthodox', 'detest', 'sway', 'engross', 'delusion', 'transplant', 'improvise', 'controversial', 'predicate', 'overturn', 'manifestation', 'consecutive', 'dispatch', 'bewitch', 'lateral', 'conceit',
         'heredity', 'pungent', 'vicious', 'preach', 'punctuality', 'provocative', 'discretion', 'rehabilitation', 'stagger', 'ingest', 'predisposed', 'fabricate', 'composed', 'offset', 'outlaw', 'stout', 'metabolism', 'plausible', 'stumble', 'sellf-contained']
H = [['세입자', '임차인'], ['세게 밀다', '밀치다',  '찌름'], ['만장일치의', '이의가 없는'], ['입증하다', '실증하다', '승인하다'], ['폭군', '독재자'], ['확인하다', '승인하다',  '굳히다'], ['강요하다', '억제하다', '속박하다'], ['예비의', '준비의', '서두', '사전준비'], ['자세', '발의 위치', '입장', '태도'], ['속도', '빠름', '회전율'], ['유목의', '방랑의'], ['모양을 훼손하다', '변형시키다'], ['미신의', '미신을 믿는'], ['설득력 있는', '정곡을 찌르는', '타당한'], ['양심적인', '성실한', '세심한'], ['뒤엎다', '압도하다', '우선하다'], ['땀', '발한', '노력'], ['선행하다', '앞서다', '우선하다'], ['~의 탓으로 돌리다', '속성', '특성'], ['의도적인', '계획적인', '숙고하다', '심의하다'],
         ['막다', '방해하다'], ['가연성의', '불붙기 쉬운'], ['증명하다', '증언하다'], ['임대', '임대차 게약', '임대하다'], ['선언하다', '명시하다'], ['가난하게 하다', '저하시키다'], ['누적되는', '점점 쌓이는'], ['시행하다', '집행하다'], ['부정하다', '모순되다'], ['중단하다', '가로막다'], ['늘리다', '증가하다'], ['명성', '인기', '위신'], ['주시하다', '바라보다'], ['적용할 수 있는', '적절한', '타당한'], ['앞서서 주도하는', '솔선하는', '진취적인', '주도적인'], ['하지 않을 수 없는', '강력한', '강제적인'], ['낭비하는', '지나친', '터무니 없는'], ['인식의', '인지적인'], ['감각', '재치', '요령'], ['내쫓다', '제명하다'],
         ['휴전', '정전', '중단'], ['화해하다', '중재하다', '받아들이게 하다'], ['최고의', '최후의'], ['고갈되지 않는', '지칠 줄 모르는'], ['소환하다', '불러내다'], ['침착', '평형', '몸가짐', '평형을 유지하다', '태세를 유지하다'], ['숨 막히게 하다', '억압하다'], ['생략', '빠뜨림', '태만'], ['전술', '작전', '병법', '술책'], ['토착의', '원주민의', '원래의'], ['분개한', '성난'], ['우선시키다', '우선순위를 매기다'], ['저버리다', '도망가다', '방치하다'], ['속이는', '현혹시키는'], ['체류하다', '묵다', '체류', '체재', '기숙'], ['자랑하다', '뽐내다', '자랑', '허풍'], ['비통한', '슬픈', '심한', '가혹한'], ['조급함', '참을 수 없음'], ['코를 골다', '코 골기'], ['환대', '수용'],
         ['포로의', '사로잡힌', '포로'], ['농축하다', '요약하다', '간추리다'], ['이끌어 내다', '유도해내다'], ['영앙분이 많은'], ['떨리다', '진동', '떨림'], ['비우다', '피난시키다'], ['선거의', '유권자의'], ['권위적인', '권위주의적인'], ['굉장히 무서운', '몹시 싫은', '끔찍한'], ['경멸하다', '경멸', '무시'], ['의견', '생각', '소감', '감정', '기분', '정서'], ['인과 관계의', '원인이 되는'], ['유혹적인', '매력적인'], ['맛', '풍미', '재미', '즐기다', '음미하다'], ['토착의', '타고난', '고유한'], ['비난하다', '선고하다', '유죄판결을 내리다'], ['독재자', '지배자'], ['(불을) 끄다', '소멸시키다'], ['표준', '척도', '규범'], ['왕좌', '왕위'],
         ['설득하다', '확신시키다'], ['화물', '차에 싣는 짐'], ['긴급한', '중요한', '명령', '필요성'], ['재주가 있는', '자원이 풍부한'], ['은혜를 모름', '배은망덕'], ['회전하다', '돌다'], ['초라한', '누추한', '비열한'], ['증명하다', '보증하다'], ['단언하다', '주장하다'], ['환상을 깨뜨리다', '각성', '환멸'], ['포괄적인', '종합적인'], ['숨을 들이쉬다', '흡입하다'], ['분리하다', '차별하다'], ['파다', '발굴하다'], ['오물', '시궁창 물'], ['결혼의', '부부의', '남편의'], ['기울다', '기울기', '경사'], ['배치하다', '전개하다', '활용하다'], ['겁주다', '협박하다', '위협하다'], ['떼어놓다', '분리시키다'],
         ['다투다', '싸우다', '경쟁하다'], ['역의', '반대의', '거꾸로 된'], ['촉매', '자극제', '계기'], ['이타적인'], ['자세', '태도'], ['온전한', '손상되지 않은'], ['담그다', '가라앉히다', '몰두시키다'], ['가로지르다', '횡단하다'], ['경건한', '신앙심이 깊은'], ['맛보다', '음미하다', '맛', '풍미'], ['운문','시'], ['조르다', '질식시키다', '교살하다'], ['인질', '담보'], ['경솔한', '성급한', '지각없는'], ['맹세하다', '서약하다', '맹세', '서약', '저당'], ['일관성 없는', '일치하지 않는', '모순된'], ['배신자', '반역자', '역적'], ['근거 없는', '(사실) 무근의'], ['암시[함축]', '함축적 의미'], ['소외시키다', '주류에서 몰아내다'],
         ['입법부', '국회'], ['반박하다', '되쏘아 붙이다', '말대꾸', '반박'], ['간청하다', '변명하다'], ['엄한', '험악한', '무자비한'], ['압도하다', '당황하게 하다'], ['연약한', '깨지기 쉬운'], ['가라앉다', '침몰하다'], ['인내', '끈기', '불굴의 노력'], ['공예가', '장인[기능공]'], ['점착성의', '끈끈한', '접착제'], ['숙지시키다', '알게하다'], ['새것으로 만들다', '수리하다', '혁신하다'], ['충분히 만족시키다', '물리게 하다'], ['진술', '주장', '명제', '제의', '일', '문제'], ['붐비게하다', '가득 채우다'], ['틀렸음을 입증하다', '반증하다', '반박하다'], ['중립화하다', '중화하다'], ['부분', '조각', '단편', '나누다', '분할하다'], ['남자의', '남성적인'], ['되풀이되는', '재발하는'],
         ['깊이 생각하다', '숙고하다'], ['들어갈 수 없는', '이해할 수 없는'], ['임신한'], ['고요함', '평온함', '침착'], ['가설을 세우다', '가정하다'], ['주입하다', '스며들게 하다'], ['경멸하다', '혐오하다', '깔보다'], ['뿌리 뽑다', '근절하다'], ['현장', '발생지', '장소'], ['불충분한', '부족한', '빈약한', '빠듯한'], ['배심원단', '심사원단'], ['약화시키다', '혼합하다', '절충하다', '혼합의', '혼합물'], ['무차별적인', '가리지 않는', '난잡한'], ['진압하다', '억누르다', '억제하다'], ['신뢰하다', '털어놓다'], ['강조하는', '단호한', '확실한'], ['형제자매'], ['발생', '발생률'], ['변경', '조절'], ['양극화하다', '편향하다'],
         ['공정한', '치우치지 않은'], ['조율하다', '맞추다'], ['무식한', '교육받지 못한', '무례한', '모르는'], ['자기도 모르게 하는', '마지못해 하는', '본의 아닌'], ['가하다', '괴롭히다'], ['겉치레', '가장', '부당한 주장'], ['영속시키다', '불멸하게 하다'], ['위생적인', '건강에 좋은'], ['거주하다', '살다', '차지하다'], ['오르다', '상승하다'], ['공평함'], ['빈정대는', '비꼬는', '풍자적인'], ['떨다', '전율하다', '떨림', '전율'], ['황폐화시키다', '철저히 파괴하다'], ['사상자', '희생자'], ['언급하다', '문의하다', '돌리다', '귀속시키다'], ['손상시키다', '(가치를) 떨어뜨리다', '비방하다'], ['온화한', '적당한', '절제된', '중용의'], ['구두점을 찍다', '중단시키다'], ['상원', '원로원'],
         ['고집 센', '완고한'], ['짖궂은', '개구쟁이의', '해를 끼치는', '악영향의'], ['불합리', '모순', '어리석음'], ['참호를 파다', '단단히 자리 잡다', '확립하다'], ['속물', '고상한 척 하는 사람'], ['응집성의', '결합력이 있는'], ['현명함', '분별', '신중'], ['힘든', '고된', '요구가 많은'], ['자치의', '자율적인'], ['지침', '가르침'], ['떨다', '몸서리치다', '진동하다', '떨림', '전율'], ['임차', '보유', '재직'], ['공중위생', '위생 시설'], ['독창적인', '영리한'], ['밟다', '걷다', '밟기', '발걸음', '발바닥'], ['여행 스케줄', '여행 계획'], ['예의바른', '정중한'], ['딴 데로 돌리다', '전환한다'], ['유죄를 선고하다', '유죄 선고 받은 사람', '죄수'], ['분열', '혼란'],
         ['오르내리다', '동요하다'], ['도살', '살육', '도살하다', '살육하다'], ['강박 관념', '~에 사로잡힘'], ['유인하다', '유혹하다', '매력', '유혹'], ['건조시키다', '탈수 상태가 되다'], ['부추기다', '선동하다'], ['겁쟁이', '비겁자'], ['직업', '천직', '소명[하늘의 부르심]'], ['동정심이 많은', '인정 많은'], ['사소한', '하찮은', '평범한', '진부한'], ['시골뜨기', '촌놈', '시골의', '소박한'], ['강력히 권하다', '열심히 설득하다', '충고하다'], ['비행', '항공기'], ['익명'], ['구부릴 수 없는', '경직된'], ['다재다능한', '만능의'], ['도움이 되는', '기여하는'], ['설교', '훈계', '잔소리'], ['손상', '파괴', '부패'], ['갈망하다', '동경하다'],
         ['크게 승리한', '성공한', '의기양양한', '승리에 취한'], ['수도자'], ['향기', '향수'],['독점', '전매'], ['분해하다', '부패하다'], ['접근하기 어려운', '걷기 힘든'], ['예방', '저지', '방해'], ['지상의', '세속적인', '평범한', '재미없는'], ['위선의', '위선적인'], ['비만인', '뚱뚱한'], ['강제적인', '의무적인', '필수적인'], ['복제하다', '복사하다', '똑같은 것', '사본', '복제품'], ['삼가다', '자제하다', '후렴구', '자주 반복되는 말'], ['떨어져 있는', '분리된', '공평한', '객관적인', '초연한'], ['장례식'], ['상투적인 말', '틀에 박힌', '진부한'], ['후회하다', '참회하다'],['효능', '효력'],['문외한', '비전문가', '평신도'], ['늘리다', '연장하다'],
         ['공감하다', '감정 이입하다'], ['열대지방의 농장', '농원'], ['갉아먹다', '침식하다', '괴롭히다'], ['성질', '기질', '기분', '조절하다', '단련하다'], ['초월하다', '능가하다'], ['완고한', '외고집의'], ['인색한', '쩨쩨한', '부족한'], ['숨다', '잠복하다'], ['의기양양한', '우쭐대는', '마냥 신난'], ['술 취하지 않은', '냉정한', '술을 깨다', '냉정해지다'], ['애원하다', '간청하다'], ['정복', '승리', '획득'], ['돌이킬 수 없는', '취소할 수 없는'], ['풍부한', '넓은', '풍만한'], ['근본적인', '아래에 놓여 있는', '숨겨진'], ['유사한', '비슷한'], ['괴리', '차이', '불일치'], ['불충분한', '부적당한'], ['정당화', '명분', '변명'], ['느슨한', '꾸물거리는', '느슨함', '늘어짐', '처짐'],
         ['결정적인', '최종적인', '명확한'], ['분배하다', '베풀다', '~없이 지내다', '필요 없게 하다'], ['강탈하다', '횡령하다', '표절하다'], ['반란자', '반항자', '반란을 일으키다', '반항하다'], ['동시에 일어나다', '일치하다', '부합하다'], ['가루가 되다', '부서지다', '힘없이 무너지다'], ['고갈시키다', '비우다'], ['대참사', '재앙', '파국', '대단원'], ['고문하다', '괴롭히다', '비틀다', '고문', '고뇌'], ['돌연변이하다', '변화하다', '변화시키다'], ['얽힘', '혼란', '엉키다', '얽히게 되다'], ['재통일하다', '재통합하다'], ['투명한', '명백한'], ['싹트다', '성장하다'], ['저당', '대출', '융자', '저당 잡히다', '담보 대출하다'], ['호기심이 강한', '꼬치꼬치 캐묻는'], ['비난', '질책', '불명예', '비난하다', '꾸짖다'], ['구식의', '더 이상 쓸모없는'], ['폭동', '소요', '폭동을 일으키다'], ['명목상의', '이름뿐인'],
         ['배신', '밀고', '배반'], ['널리 알리다', '광고하다', '선전하다'], ['코를 킁킁거리다', '냄새 맡다', '코를 킁킁거림'], ['화려한', '훌륭한', '멋진'], ['비정통적인', '인습적이지 않은'], ['혐오하다', '몹시 싫어하다'], ['흔들리다', '흔들다', '흔들림', '동요', '지배'], ['몰두시키다', '빼앗다'], ['현혹', '망상', '착각'], ['이식하다', '이식', '이주'], ['즉석에서 짓다', '임시변통하다'], ['쟁점이 되는', '토론을 좋아하는'], ['단정하다', '근거를 두다', '입각하다'], ['뒤집다', '전복하다', '전복', '붕괴'], ['명시', '표명', '출현', '발현'], ['연속적인', '앞뒤가 맞는'], ['급파하다', '신속히 처리하다', '급파', '신속한 처리'], ['흘리다', '매료시키다', '넋을 빼앗다'], ['옆의', '측면의', '방계의'], ['자부심', '자만심'],
         ['유전', '유전적 특징'], ['자극적인', '신랄한', '날카로운'], ['나쁜', '악랄한', '잔인한'], ['설교하다', '전도하다'], ['시간 엄수', '정확함'], ['자극적인', '화나게 하는'], ['사려분별', '신중함', '재량'], ['갱생', '재활', '회복', '복직'], ['비틀거리다', '흔들리다', '깜짝 놀라게 하다'], ['섭취하다', '받아들이다'], ['~하기 쉬운 경향이 있는'], ['만들다', '제작하다', '위조하다'], ['침착한', '평온한'], ['상쇄하다', '벌충하다', '상쇄', '벌충', '보충'], ['불법화하다', '금지하다', '무법자', '상습범'], ['뚱뚱한', '비만한', '튼튼한', '강한', '단호한', '용감한'], ['신진대사', '대사작용'], ['그럴듯한', '정말 같은'], ['발부리가 걸리다', '비틀거리다', '더듬다', '우연히 발견하다'], ['자급자족인', '독립적인', '말수가 적은', '자제하는']]

problem_H = [] #한글 문제 리스트
problem_E = [] #영어 문제 리스트

n=0
n1=0
n2=0
n3=0
n4=0
n5=0
n6=0
n7=0
n8=0
n9=0
n10=0
n11=0
n12=0
n13=0
n14=0
n15=0
n16=0
answer=''
an=''
nWord=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
score = 0 # 총점수
score_Part = 0 # 부분 점수(초기화용)
cnt = 0 # 부분 점수(합산용)
cnt_mola  = 0 # 부분 점수로 계산 시 문제의 개수
problem=''
temanswer=0
display_temanswer=0
inscore=0
        

a=''
b=0
class frontend(QMainWindow, form_class):
    global n1
    global n2
    global n3
    global n4
    global n5
    global n6
    global n7
    global n8
    global n9
    global n10
    global n11
    global n12
    global n13
    global n14
    global n15
    global n16
    global nWord
    global answer
    global n
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon("영단어 시험프로그램 아이콘")) 
        self.setWindowTitle("영단어 시험 프로그램 v2")
        self.initialize.clicked.connect(self.initializing)
        self.closebtn.clicked.connect(self.close)
        self.OK.clicked.connect(self.checkfunction)
        self.OK.clicked.connect(self.makeproblemlist)
        self.OK.clicked.connect(self.examproblem)
        self.answerinput.returnPressed.connect(self.answercheck)



    def initializing(self):
        global a
        global nWord
        global problem_H
        global problem_E
        global score
        global score_Part
        global cnt
        global cnt_mola
        global answer
        global an
        global temanswer
        global display_temanswer
        global inscore
        answer=''
        an=''
        nWord=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        score = 0 
        score_Part = 0 
        cnt = 0
        cnt_mola  = 0 
        problem=''
        temanswer=0
        display_temanswer=0
        inscore=0
        
        self.problem.setText('')
        self.beforeproblem.setText('')
        self.answermean.setText('')
        self.partNanswer.setText('0')
        self.partNinanswer.setText('0')
        self.Nanswermean.setText(str(display_temanswer))
        self.Nscore.setText('0')
        self.Ninscore.setText('0')
        self.answer_n.setText('')
        
        self.answerinput.setText('')

    def checkfunction(self):#체크된 박스 확인
        if self.checkBox.isChecked() : nWord[1]=1
        if self.checkBox_2.isChecked() : nWord[2]=2
        if self.checkBox_3.isChecked() : nWord[3]=3
        if self.checkBox_4.isChecked() : nWord[4]=4
        if self.checkBox_5.isChecked() : nWord[5]=5
        if self.checkBox_6.isChecked() : nWord[6]=6
        if self.checkBox_7.isChecked() : nWord[7]=7
        if self.checkBox_8.isChecked() : nWord[8]=8
        if self.checkBox_9.isChecked() : nWord[9]=9
        if self.checkBox_10.isChecked() : nWord[10]=10
        if self.checkBox_11.isChecked() : nWord[11]=11
        if self.checkBox_12.isChecked() : nWord[12]=12
        if self.checkBox_13.isChecked() : nWord[13]=13
        if self.checkBox_14.isChecked() : nWord[14]=14
        if self.checkBox_15.isChecked() : nWord[15]=15
        if self.checkBox_16.isChecked() : nWord[16]=16        
        
    def ncheck(self):
        n=self.answercount.text()
        #read only 활성화법 입력 예정
        
        

        

   # def makeproblem(self)


    def makeproblemlist(self):
        global a
        global nWord
        global problem_H
        global problem_E
        global score
        global score_Part
        global cnt
        global cnt_mola
        global answer
        global an


        a=''
        a = nWord
        nWord=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        problem_H=[]
        problem_E=[]

        for i in range(len(a)):
            if a[i] == 1:
                for j in range(20):
                    problem_H.append(H[j])
                    problem_E.append(E[j])
            elif a[i] == 2:
                for j in range(20,40):
                    problem_H.append(H[j])
                    problem_E.append(E[j])
            elif a[i] == 3:
                for j in range(40, 60):
                    problem_H.append(H[j])
                    problem_E.append(E[j])
            elif a[i] == 4:
                for j in range(60, 80):
                    problem_H.append(H[j])
                    problem_E.append(E[j])
            elif a[i] == 5:
                for j in range(80, 100):
                    problem_H.append(H[j])
                    problem_E.append(E[j])
            elif a[i] == 6:
                for j in range(100, 120):
                    problem_H.append(H[j])
                    problem_E.append(E[j])

            elif a[i] == 7:
                for j in range(120, 140):
                  problem_H.append(H[j])
                  problem_E.append(E[j])
            elif a[i] == 8:
                for j in range(140, 160):
                  problem_H.append(H[j])
                  problem_E.append(E[j])
            elif a[i] == 9:
                for j in range(160, 180):
                  problem_H.append(H[j])
                  problem_E.append(E[j])
            elif a[i] == 10:
                for j in range(180, 200):
                  problem_H.append(H[j])
                  problem_E.append(E[j])
            elif a[i] == 11:
                for j in range(200, 220):
                  problem_H.append(H[j])
                  problem_E.append(E[j])
            elif a[i] == 12:
                for j in range(220, 240):
                  problem_H.append(H[j])
                  problem_E.append(E[j])
            elif a[i] == 13:
                for j in range(240, 260):
                  problem_H.append(H[j])
                  problem_E.append(E[j])
            elif a[i] == 14:
                for j in range(260, 280):
                  problem_H.append(H[j])
                  problem_E.append(E[j])
            elif a[i] == 15:
                for j in range(280, 300):
                  problem_H.append(H[j])
                  problem_E.append(E[j])
            elif a[i] == 16:
                for j in range(300, 320):
                  problem_H.append(H[j])
                  problem_E.append(E[j])


    def examproblem(self):
        global a
        global b
        global nWord
        global problem_H
        global problem_E
        global score
        global score_Part
        global cnt
        global cnt_mola
        global answer
        global an
        global n
        global problem

        #a 출제할 문제
        #b 출제할 문제의 인덱스
        #an 입력한 답(answer)
        #n 전체문제 개수
        #cnt_mola 부분문제 개수
        #score 전체문제 정답수
        #cnt 부분문제 정답수
        #

        #문제 출제
        problem = r.choice(problem_E) # 섞기
        self.problem.setText(problem)
        print(problem)

            
      
        for i in range(len(problem_E)):
            if problem == problem_E[i]:
                b = i # 리스트의 인덱스 저장
        
        if len(problem_H[b]) == 1: # 답이 한 개 일 경우
            cnt_mola += 1
            self.answer_n.setText('1개')

        elif len(problem_H[b]) == 2: # 답이 두 개 일 경우
            cnt_mola += 2
            self.answer_n.setText('2개')

        elif len(problem_H[b]) == 3: # 답이 세 개 일 경우
            cnt_mola += 3
            self.answer_n.setText('3개')

        elif len(problem_H[b]) == 4: # 답이 네 개 일 경우
            cnt_mola += 4
            self.answer_n.setText('4개')

        elif len(problem_H[b]) == 5: # 답이 다섯 개 일 경우
            cnt_mola += 5
            self.answer_n.setText('5개')


    def answercheck(self):              #enter 누르면 작동
        global a
        global b
        global nWord
        global problem_H
        global problem_E
        global score
        global score_Part
        global cnt
        global cnt_mola
        global answer
        global an
        global n
        global problem
        global temanswer
        global display_temanswer
        global inscore

        
        answer=self.answerinput.text()
        print(answer)
        self.answerinput.setText('')



        temanswer=0
        an = str(answer)
        print(an)
        print(problem_H[b])

        if len(problem_H[b]) == 1: # 답이 한 개 일 경우
            if an == str(problem_H[b][0]):
                #self.answer_OX.setText('정답!')
                score += 1
                score_Part += 1
                cnt_mola -= 1
                temanswer+=1
                display_temanswer+=1
            else:
                #self.answer_OX.setText("오답")
                inscore+=1





        else:
            if len(problem_H[b]) == 2: #답이 2개인 경우
                an = list(answer.split(','))
                an.sort()
                problem_H[b].sort()
                print(an)
                print(problem_H[b])
                for k in range(len(an)):
                    for j in range(len(problem_H[b])):
                        if str(an[k]) == str(problem_H[b][j]):
                            score_Part += 1
                            cnt += 1
                            cnt_mola-=1
                            temanswer+=1
                            display_temanswer+=1

                                   
                if temanswer==len(problem_H[b]): #답을 다 맞힌 경우
                    score += 1
                    #self.answer_OX.setText('정답!')
                else:
                    inscore+=1


            elif len(problem_H[b]) == 3: #답이 3개인 경우
                an = list(answer.split(','))
                an.sort()
                problem_H[b].sort()
                for k in range(len(an)):
                    for j in range(len(problem_H[b])):
                        if an[k] == problem_H[b][j]:
                            score_Part += 1
                            cnt += 1
                            cnt_mola-=1
                            temanswer+=1
                            display_temanswer+=1
                            
                if temanswer == len(problem_H[b]):
                    score += 1
                else:
                    inscore+=1

            elif len(problem_H[b]) == 4: #답이 4개인 경우
                an = list(answer.split(','))
                an.sort()
                problem_H[b].sort()
                for k in range(len(an)):
                    for j in range(len(problem_H[b])):
                        if an[k] == problem_H[b][j]:
                            score_Part += 1
                            cnt += 1
                            cnt_mola-=1
                            temanswer+=1
                            display_temanswer+=1
                            
                if temanswer == len(problem_H[b]):
                    score += 1
                else:
                    inscore+=1


            elif len(problem_H[b]) == 5: #답이 5개인 경우
                an = list(answer.split(','))
                an.sort()
                problem_H[b].sort()
                for k in range(len(an)):
                    for j in range(len(problem_H[b])):
                        if an[k] == problem_H[b][j]:
                            score_Part += 1
                            cnt += 1
                            cnt_mola-=1
                            temanswer+=1
                            display_temanswer+=1
                            
                if temanswer == len(problem_H[b]):
                    score += 1
                else:
                    inscore+=1

            elif len(problem_H[b]) == 6: #답이 6개인 경우
                an = list(answer.split(','))
                an.sort()
                problem_H[b].sort()
                for k in range(len(an)):
                    for j in range(len(problem_H[b])):
                        if an[k] == problem_H[b][j]:
                            score_Part += 1
                            cnt += 1
                            cnt_mola-=1
                            temanswer+=1
                            display_temanswer+=1
                            
                if temanswer == len(problem_H[b]):
                    score += 1
                else:
                    inscore+=1


        self.beforeproblem.setText(str(problem))
        self.answermean.setText(str(problem_H[b]))
        self.partNanswer.setText(str(score_Part))
        self.partNinanswer.setText(str(cnt_mola))
        self.Nanswermean.setText(str(display_temanswer))
        self.Nscore.setText(str(score))
        self.Ninscore.setText(str(inscore))
        display_temanswer=0

        self.examproblem()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    execution = frontend()
    execution.show()
    app.exec_()
