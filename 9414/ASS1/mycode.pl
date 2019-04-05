% COMP9414 Assignment 1 - Prolog Programming
% Author : SIJIE HOU
% StudentID : z5193712

%question 1

is_even(X) :-
	Y is X//2,
	X =:= Y * 2.

is_odd(X) :-
	Y is X mod 2,
	Y =:=1.

	
square(Num,Value):-
	Value is Num * Num.

sumsq_even([],0).

sumsq_even([H|T], Sum) :-
	is_even(H),	
	sumsq_even(T,Result),
	square(H,Value),
	Sum is Result + Value.
	
sumsq_even([H|T], Sum) :-
	is_odd(H),
	sumsq_even(T,Sum).


%question 2
%the variable must be start with capital letter,which means title

is_Maleancestor(Ancestor,Child):-
	parent(Ancestor,Child),
	male(Ancestor).

is_Maleancestor(Ancestor,Child):-
	parent(Ancestor,Parent),
	male(Ancestor),
	is_Maleancestor(Parent,Child).

%one is another ancesotr
same_name(Person1,Person2):-
	is_Maleancestor(Person1,Person2).

same_name(Person1,Person2):-
	is_Maleancestor(Person2,Person1).

%same ancestor	

same_name(Person1,Person2):-
	is_Maleancestor(Parent,Person1),
	is_Maleancestor(Parent,Person2).
	
	

%question 3

sqrt_list([], []).

sqrt_list([H|T], [RH|RT]):-	
	sqrt_list(T, RT),
	H >= 0,	
	X is sqrt(H),
	RH = [H,X].






%question 4

is_negative(X,Res):-
	X>=0,
	Res = 1.

is_negative(X,Res):-
	X<0,
	Res = 0.


%find the sametype 
sametype([],_,[],[]).

sametype([Head|Tail], Type ,Result, ListTail) :-
	is_negative(Head,OneOrO),
	OneOrO =:= Type,
	sametype(Tail, Type, RestResult, ListTail),
	Result = [Head|RestResult].

sametype([Head|Tail], Type , [], [Head|Tail]) :-
	is_negative(Head,OneOrO),
	OneOrO =\= Type.


%is the same tpye ,add

sign_runs([],[]).

sign_runs([Head|Tail],RunList) :-
	is_negative(Head,OneOrO),
	sametype([Head|Tail], OneOrO, Result, ListTail),
	sign_runs(ListTail,RestResult),
	RunList = [Result|RestResult].





	
	

%question 5
%node less than child


tree_value(tree(_,Value,_),Value).

is_heap(tree(empty,_,empty)).
is_heap(empty).


is_heap(tree(Leftnode,Node,Rightnode)) :-
	tree_value(Leftnode,LeftValue),
	tree_value(Rightnode,RightValue),
	Lefttree = Leftnode,
	Righttree = Rightnode,
	
	Node =< LeftValue,
	Node =< RightValue,
	is_heap(Lefttree),
	is_heap(Righttree).




is_heap(tree(empty,Node,Rightnode)):-
	tree_value(Rightnode,RightValue),
	Righttree =Rightnode,
	Node =<RightValue,	
	is_heap(Righttree).



is_heap(tree(Leftnode,Node,empty)):-
	tree_value(Leftnode,LeftValue),
	Lefttree = Leftnode,
	Node =<LeftValue,
	is_heap(Lefttree).
	
	