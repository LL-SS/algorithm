class Node:
    """링크드 리스트의 노드 클래스"""

    def __init__(self, data):
        self.data = data # 실제 노드가 저장하는 데이터
        self.next = None # 다음 노드에 대한 레퍼런스
        self.prev = None # 이전 노드에 대한 레퍼런스


class LinkedList:
    """링크드 리스트 클래스"""

    def __init__(self):
        self.head = None # 링크드 리스트의 가장 앞 노드
        self.tail = None # 링크드 리스트의 가장 뒤 노드

    def find_node_with_data(self, data):
        """링크드 리스트에서 탐색 연산 메소드. 단, 해당 노드가 없으면 None을 리턴한다"""
        # 코드를 쓰세요
        iterator = self.head

        while iterator is not None:
            if iterator.data == data:
                return iterator

            iterator = iterator.next

        return None

    def find_node_at(self, index):
        """링크드 리스트 접근 연산 메소드. 파라미터 인덱스는 항상 있다고 가정"""
        iterator = self.head

        for _ in range(index):
            iterator = iterator.next

        return iterator

    def append(self, data):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(data)

        # 링크드 리스트가 비어 있으면 새로운 노드가 링크드 리스트의 처음이자 마지막 노드다
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # 링크드 리스트가 비어 있지 않으면
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def prepend(self, data):
        """링크드 리스트의 가장 앞에 데이터 삽입"""
        # 코드를 쓰세요
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_after(self, previous_node, data):
        """링크드 리스트 주어진 노드 뒤 삽입 연산 메소드"""
        new_node = Node(data)

        if previous_node is self.tail:
            previous_node.next = new_node
            new_node.prev = previous_node
            self.tail = new_node

        else:
            new_node.prev = previous_node
            new_node.next = previous_node.next
            previous_node.next = new_node
            previous_node.next.prev = new_node

    def delete(self, node_to_delete):
        """더블리 링크드 리스트 삭제 연산 메소드"""

        # 링크드 리스트에서 마지막 남은 데이터를 삭제할 때
        if node_to_delete is self.head and node_to_delete is self.tail:
            self.tail = None
            self.head = None

        # 링크드 리스트 가장 앞 데이터 삭제할 때
        elif node_to_delete is self.head:
            self.head = self.head.next
            self.head.prev = None

        # 링크드 리스트 가장 뒤 데이터 삭제할 떄
        elif node_to_delete is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None

        # 두 노드 사이에 있는 데이터 삭제할 때
        else:
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev

        # 삭제하는 노드 데이터 리턴
        return node_to_delete.data

    def __str__(self):
        """링크드  리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = "|"

        # 링크드  리스트 안에 모든 노드를 돌기 위한 변수. 일단 가장 앞 노드로 정의한다.
        iterator = self.head

        # 링크드  리스트 끝까지 돈다
        while iterator is not None:
            # 각 노드의 데이터를 리턴하는 문자열에 더해준다
            res_str += " {} |".format(iterator.data)
            iterator = iterator.next  # 다음 노드로 넘어간다

        return res_str

# 새로운 링크드 리스트 생성
my_list = LinkedList()

# 새로운 노드 4개 추가
my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)

print(my_list)

# 두 노드 사이에 있는 노드 삭제
node_at_index_2 = my_list.find_node_at(2)
my_list.delete(node_at_index_2)
print(my_list)

# 가장 앞 노드 삭제
head_node = my_list.head
print(my_list.delete(head_node))
print(my_list)

# 가장 뒤 노드 삭제
tail_node = my_list.tail
my_list.delete(tail_node)
print(my_list)

# 마지막 노드 삭제
last_node = my_list.head
my_list.delete(last_node)
print(my_list)