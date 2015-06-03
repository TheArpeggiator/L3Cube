/*The birthday paradox is a scenario where people expect that with a lower number of people there is a smaller chance of two people sharing the same birthday. But this is not true and this is the birthday paradox which is proved by this program. Reaches a probability of 0.99  at approximately 70 people */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
	int peeps,pairs;
	float safe,prob;

	printf("\nEnter number of people to check for same birthday:\n");
	scanf("%d",&peeps);

	pairs=(peeps*(peeps-1))/2;	//total number of possible pairs 
	safe=(364.00/365.00);		//probabilty of 2 people not sharing b'day

	prob=1-pow(safe,pairs);		//probability of a pair sharing a birthday

	printf("\nProbabilty of a pair sharing birthday: %f\n",prob);
	return 0;
}
