sigma.png : bayes.py valores.txt
	@python bayes.py
solar.png : bayes.py monthrg.dat
	@python bayes.py
./a.out : tres.cpp
	@c++ tres.cpp -o ./a.out


	
clean :
	rm -f *.png
