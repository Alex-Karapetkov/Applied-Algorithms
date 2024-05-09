Finding an Arbitrage
In currency exchange markets units of one currency, such as US Dollars, can be exchanged for units of a different currency, like Italian Lira. These exchanges are set by the market's exchange rate, which typically fluctuates throughout the day. For example, at the time of this assignment's writing, the exchange rate between the US Dollar (USD) and the Great British Pound (GBP) was 1 USD to 0.77 GBP. This means that $150 is worth 150*0.77=115.5 GBP and 150 GPB = 150 / 0.77 = $194.81. The exchange rates are dynamic and constantly change.

This change in currency is based on how trades are progressing through the market, and the changing dynamic nature of the exchange leads to a particular inefficiency in short-time frame based trading.  For example, consider the following exchange rates: 

1 USD = 0.82 Euro
 1 Euro = 129.7 Japanese Yen
1 Japanese Yen = 12 Turkish Lira
1 Turkish Lira = 0.0008 USD. 

So if we start with 1 USD, and make all of the exchanges above, we get 1*0.82*129.7*12*.0008 = $1.021. In other words, by making four exchanges starting from $1.00 we end up with $1.02, a 2% profit. This situation, where a cycle of currency exchanges starting and ending in the same currency leads to a net gain in the starting currency (rather than breaking even) is called arbitrage.

Notice that arbitrage occurs when the product of all of the exchanges in a cycle is greater than 1. Your job is to find and detect arbitrage in a given exchange and determine what sequence of exchanges need to be made. 

We are going to reduce this problem to the problem of finding negative weight cycles in a graph. There are two problems to overcome. 

Our formulation of the problem requires a product of the exchange rates, but shortest path algorithms work with the sum of the weights of a bunch of edges. 
Negative weight cycles are "smaller" whereas we are attempting to maximize a profit. 
The first problem can be overcome using the following trick: the logarithm function is monotonic, which means that log(x) increases when x increases. Furthermore, the logarithm function can be used to convert products into sums because log(a * b) = log(a) + log(b). Thus, if we want to maximize a*b, this is the same as maximizing log(a) + log(b). Also, consider that a * b > 1 if and only if log(a) + log(b) > 0. Thus a cycle of exchange rates r1 * r2 * r3 * ... * rn > 1 if and only if log(r1) + log(r2) + ... + log(rn) > 0. 

But now the second problem is that we want to detect negative weight cycles because Bellman-Ford can do that for us, but above we described a positive weight cycle. Now we can use the following trick--simply negate each log value. log(r1) + log(r2) + ... + log(rn) > 0 if and only if (-log(r1)) + (-log(r2)) + ... + (-log(rn)) < 0. Now, you should be able to see how to build a graph, with some appropriate weights, and use it to find arbitrage cycles directly!

Input
The first line of the input will contain a single integer m describing how many exchange rates are in the exchange. The next m lines will be given by cIn cOut r where cIn is the code for the starting currency (like USD or GPB), cOut is the code for the ending currency, and r is the exchange rate (i.e. "USD GBP 0.75" codes for 1 USD = 0.75 GBP). 

Output and Rubrics
This assignment is worth 15 points.

9 points (partial) -- code identifies an the presence or absence of an arbitrage correctly on published test cases
3 points (partial) -- code  identifies an the presence or absence of an arbitrage correctly on hidden test cases
2 points (full credit) -- code outputs the actual exchanges correctly and in the format specified on the public test cases
1 point  (full credit) -- code outputs the actual exchanges correctly and in the format specified on the hidden test cases
For full credit, when an arbitrage is detected, in addition to the output above, your code should output the actual exchanges that need to be made by showing each currency code in the exchange separated by " => " on a second line, and a third line containing the actual change as a multiplicative factor with the format "X factor increase", which should be formatted to 5 decimal points.
