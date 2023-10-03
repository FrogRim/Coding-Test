![[Pasted image 20231003154753.png]]

```
//C++ : max-heap

priority_queue<int> pq;
pq.push(456);
pq.push(123);
pq.push(789);

printf("size: %d\n",pq.size());

while(!pq.empty()){
	printf("%d\n",pq.top());
	pq.pop();
}
```

```
#Python : min-heap

import heapq

pq = []
heapq.headpush(pq,456)
heapq.headpush(pq,123)
heapq.headpush(pq,789)

print("size ",len(pq))
while len(pq) > 0:
	print(heapq.headpop(pq))
```

- 이진트리 기반 
- 삽입/삭제 : O(logN)
- <span style="color:red"> C++은 큰 값부터 Python은 작은 값부터 나온다</span>
- Root node(최상단 노드)에 최댓값이 들어가면 max-heap, 최소값이 들어가면 min-heap이다.