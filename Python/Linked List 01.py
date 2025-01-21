

#.....................................Linked List

class Node:
    def __init__(self,data,next_obj):
        self.data=data
        self.next_obj=next_obj
  
class Linkedlist:
    def __init__(self):
        self.head=None

    def insert_at_begining(self,data):
        node=Node(data,self.head)
        self.head=node
    def display_data(self):
        itr=self.head
        linked_list=''
        while itr:
            suffix=''
            nxt=None
            if itr.next_obj:
                suffix +='-->'
                nxt='Next'
            #linked_list +=f'[{str(itr.data)}|{str(itr.next_obj)}]'+suffix
            linked_list +=f'[{str(itr.data)}|{nxt}]'+suffix
            itr=itr.next_obj
        print(linked_list)
    def get_length(self):
        itr=self.head
        count=0
        while itr.next_obj:
            count+=1
            itr=itr.next_obj
        return count
            
    def insert_at_last(self,data):
        itr=self.head
        if itr is None:
            self.head=Node(data,None)
            return
        while itr.next_obj:
            itr=itr.next_obj
        itr.next_obj=Node(data,None)
    
    def insert_at_n(self,data,index):
        itr=self.head
        if index <0 or index > self.get_length():
            raise Exception('Invalid index provided')
        elif index==0:
            self.insert_at_begining(data)
            return
        else:
            count=0
            while itr:
                if count==index-1:
                    node=Node(data,itr.next_obj)
                    itr.next_obj=node
                itr=itr.next_obj
                count+=1
                
            
    
add_data=Linkedlist()
add_data.insert_at_begining(5)
add_data.insert_at_begining(6)
add_data.insert_at_begining(1)
add_data.insert_at_begining(4)
add_data.insert_at_begining(8)
add_data.display_data()
add_data.insert_at_last(7)
add_data.insert_at_last(10)
add_data.insert_at_last(12)
add_data.insert_at_last(15)
add_data.display_data()
add_data.insert_at_n(70,2)
add_data.insert_at_n(80,3)
add_data.insert_at_n(90,4)
add_data.insert_at_n(1000,0)
add_data.display_data()
