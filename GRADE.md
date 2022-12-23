Dear Student,

I'm happy to announce that you've managed to get **41** out of 45 points for this assignment.\
There still exist some issues that should be addressed before the deadline: 2022-12-24 08:00:00 CET (+0100). For further details, please refer to the following list:

<details><summary>Expand frontier update labeled state if it finds better state &gt;&gt; &#x27;SearchProcess&#x27; object has no attribute &#x27;update_frontier&#x27;</summary></details>
<details><summary>Expand frontier lower bound updates &gt;&gt; lower bound was expected to change value to &#x27;3&#x27; because the new cost is better; instead it has stayed the same</summary></details>
<details><summary>Expand frontier not expands states scanned by another process &gt;&gt; expected not to expand node visited by opposite process</summary>&nbsp;- [graph](https://dreampuf.github.io/GraphvizOnline/#digraph%20G%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20S%20%20%20%5Bxlabel%3D%22scanned_by_primary%22%2Cfillcolor%3D%22darkslategray%22%2Cstyle%3D%22filled%22%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20S01%20%5Bxlabel%3D%22scanned_by_primary%22%2C%20fillcolor%3D%22darkslategray%22%2Cstyle%3D%22filled%22%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20S02%20%5Bxlabel%3D%22primary_frontier%22%2C%20fillcolor%3D%22gold3%22%2Cstyle%3D%22filled%22%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20S03%20%5Bxlabel%3D%22scanned_by_opposite%22%2Cfillcolor%3D%22darkgreen%22%2Cstyle%3D%22filled%22%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20G%20%20%20%5Bxlabel%3D%22goal%20%2B%20scanned_by_opposite%22%2Cfillcolor%3D%22darkgreen%22%2Cstyle%3D%22filled%22%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20S%20-%3E%20S01%20-%3E%20S02%20-%3E%20S03%20-%3E%20G%0A%20%20%20%20%20%20%20%20%7D)</details>
<details><summary>Select candidate not selects state if estimated cost is higher than the upper bound &gt;&gt; expected candidate with higher estimated cost to be added to the rejected states</summary></details>

-----------
I remain your faithful servant\
_Bobot_