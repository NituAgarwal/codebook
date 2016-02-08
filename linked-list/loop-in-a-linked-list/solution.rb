require_relative '../linked-list.rb'

def detect_loop(ll)
  ptr2 = ll.head.next
  ll.each do |ptr1|
    return true if ptr1 == ptr2
    return false if ptr2.nil?
    ptr2 = ptr2.next
    return false if ptr2.nil?
    ptr2 = ptr2.next
  end
end

ll = LinkedList.new(Node.new(2))
node2 = ll.insert(Node.new(3))
node3 = ll.insert(Node.new(4))
node4 = ll.insert(Node.new(6))
last = ll.insert(Node.new(5))
last.next = node4

p detect_loop(ll)
