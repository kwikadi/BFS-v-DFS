# Why

Yesterday, [dufferzafar](github.com/dufferzafar) was telling me about which was better in a 'real' world scenario to find a node in a graph, between BFS and DFS. We both agreed that BFS would take more space, but did not agree on which would run quicker. I'll spare you the entire discussion, but after quite a bit of, ahem, polite discussion, no consensus was reached.

We then decided what any CS student without much understanding of algorithmic analysis would do: We talked about how it was simple enough to design tests to see what was faster, down to the nitty gritty details. And then, like any lazy CS student, we dropped the subject and moved on to arguing about other topics (both CS and non-CS related).

Anyway, I found myself with a ton of work to do today, so I decided to procrastinate, and what better way to do it than to prove your friend wrong? So I stole the python code for BFS from GeeksForGeeks (TODO: Add link), fixed it and made some changes to suit my needs, then morphed it into DFS as well. I stole another snippet from somewhere to create a random graph, and that was it. Now, the only thing left is the tests. Shouldn't be too hard, I think.

When I do end up testing this thoroughly, I will put up time/memory numbers as well as my machine/os/python installation specs so there is some understanding of what sort of hardware/ software produces what results.

## TODO:

1. Write a shell script that takes in the number of nodes in the graph and runs each of BFS and DFS on 100 randomly generated graphs of the size given.
2. Actually add code that outputs time/space requirements
3. Tease dufferzafar if my hunch was correct, silently delete repo if it wasnt
4. Add machine specs
