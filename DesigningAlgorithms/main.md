## Designing algorithms

Designing an algorithm consists in coming up with a strictly defined sequence of activities in order to solve a given task in the most effective way. Understanding the problem involves the reference to functional and non-functional requirements. What are they about:

- Functional requirements formally indicate the input and output interface for a given problem to be solved.

- Non-functional requirements constitute a set of expectations regarding the effectiveness and safety of an algorithm.

In order to design a good algorithm, there are 3 things to keep in mind:

1. Does the algorithm return the expected result?
2. Is it doing it in an optimal way?
3. How effective will this algorithm be for large data sets?

### determining the complexity of the problem

- **Type 1.** Problems for which it can be proved that a polynomial algorithm exists for their solution.

- **Type 2.** Problems that can be proven to have no polynomial solution.

- **Type 3.** Problems for which a polynomial solution has not been found, but it cannot be proved that there is no such solution.

##### Nondetermistically polynomial problem (NP problem)

It can be proved that there is at least one polynomial algorithm that can be used to verify a potential solution.

##### Polynomial Problem (P problem)

It can be proved that there is at least one polynomial algorithm that can be used to solve them.

##### Problemy NP zupełne

Nieznane są algorytmy wielomianowe pozwalające na wygenerowanie certyfikatu. Istnieją algorytmy wielomianowe, które weryfikują czy poprawne rozwiązanie jest optymalne.

##### Problemy NP trudne

Ta klasa zawiera problemy co najmniej tak trudne, jak którykolwiek z problemów NP, ale same nie muszą należeć do problemów NP.

