male(prince_phillip).
male(prince_charles).
male(captain_mark_phillips).
male(timothy_laurence).
male(prince_andrew).
male(prince_edward).
male(prince_william).
male(prince_harry).
male(peter_phillips).
male(mike_tindall).
male(jame_viscount_severn).
male(prince_george).
male(mia_grace_tindall).

female(queen_elizabethII).
female(princess_diana).
female(camilla_paker_bowles).
female(princess_anne).
female(sarah_ferguson).
female(sophie_rhys_jones).
female(kate_middleton).
female(autumn_kelly).
female(zara_phillips).
female(princess_beatrice).
female(princess_eugenie).
female(lady_louise_mountbatten_windsor).
female(princess_charlotte).
female(savannah_phillips).
female(isla_phillips).

married(prince_phillip,queen_elizabethII).
married(queen_elizabethII,prince_phillip).
married(prince_charles,camilla_paker_bowles).
married(camilla_paker_bowles,prince_charles).
married(timothy_laurence,princess_anne).
married(princess_anne,timothy_laurence).
married(princess_edward,sophie_rhys_jones).
married(sophie_rhys_jones,princess_edward).
married(prince_william,kate_middleton).
married(kate_middleton,prince_william).
married(peter_phillips,autumn_kelly).
married(autumn_kelly,peter_phillips).
married(mike_tindall,zara_phillips).
married(zara_phillips,mike_tindall).

divorced(prince_charles,princess_diana).
divorced(princess_diana,prince_charles).
divorced(captain_mark_phillips,princess_anne).
divorced(princess_anne,captain_mark_phillips).
divorced(prince_andrew,sarah_ferguson).
divorced(sarah_ferguson,prince_andrew).

parent(queen_elizabethII,prince_charles).
parent(prince_phillip,prince_charles).
parent(queen_elizabethII,princess_anne).
parent(prince_phillip,princess_anne).
parent(queen_elizabethII,prince_andrew).
parent(prince_phillip,prince_andrew).
parent(queen_elizabethII,prince_edward).
parent(prince_phillip,prince_edward).

parent(princess_diana,prince_william).
parent(prince_charles,prince_william).
parent(princess_diana,prince_harry).
parent(prince_charles,prince_harry).

parent(captain_mark_phillips,peter_phillips).
parent(princess_anne,peter_phillips).
parent(captain_mark_phillips,zara_phillips).
parent(princess_anne,zara_phillips).

parent(sarah_ferguson,princess_beatrice).
parent(prince_andrew,princess_beatrice).
parent(sarah_ferguson,princess_eugenie).
parent(prince_andrew,princess_eugenie).

parent(sophie_rhys_jones,james_viscount_severn).
parent(prince_edward,james_viscount_severn).
parent(sophie_rhys_jones,lady_louise_mountbatten_windsor).
parent(prince_edward,lady_louise_mountbatten_windsor).

parent(prince_william,prince_george).
parent(kate_middleton,prince_george).
parent(prince_william,princess_charlotte).
parent(kate_middleton,princess_charlotte).

parent(autumn_kelly,savannah_phillips).
parent(peter_phillips,savannah_phillips).
parent(autumn_kelly,isla_phillips).
parent(peter_phillips,isla_phillips).

parent(zara_phillips,mia_grace_tindall).
parent(mike_tindall,mia_grace_tindall).

/* rules */
husband(Person,Wife):-married(Person,Wife),male(Person).
wife(Person,Husband):-married(Person,Husband),female(Person).
father(Parent,Child):-parent(Parent,Child),male(Parent).
mother(Parent,Child):-parent(Parent,Child),female(Parent).
child(Child,Parent):-parent(Parent,Child).
son(Child,Parent):-parent(Parent,Child),male(Child).
daughter(Child,Parent):-parent(Parent,Child),female(Child).

grandparent(GP,GC):-parent(GP,X),parent(X,GC).
grandmother(GM,GC):-parent(GM,X),parent(X,GC),female(GM).
grandfather(GF,GC):-parent(GF,X),parent(X,GC),male(GF).
grandchild(GC,GP):-grandparent(GP,GC).
grandson(GS,GP):-grandchild(GS,GP),male(GS).
granddaughter(GD,GP):-grandchild(GD,GP),female(GD).

sibling(Person1,Person2):-father(F,Person1),father(F,Person2),mother(M,Person1),mother(M,Person2),not(Person1=Person2).
brother(Person,Sibling):-sibling(Person,Sibling),male(Person).
sister(Person,Sibling):-sibling(Person,Sibling),female(Person).
aunt(Person,NieceNephew):-(parent(X,NieceNephew),sibling(X,Person),female(Person));(parent(X,NieceNephew),sibling(X,Y),male(Y),married(Y,Person)).
uncle(Person,NieceNephew):-(parent(X,NieceNephew),sibling(X,Person),male(Person));(parent(X,NieceNephew),sibling(X,Y),female(Y),married(Y,Person)).
niece(Person,AuntUncle):-(aunt(AuntUncle,Person),female(Person));(uncle(AuntUncle,Person),female(Person)).
nephew(Person,AuntUncle):-(aunt(AuntUncle,Person),male(Person));(uncle(AuntUncle,Person),male(Person)).