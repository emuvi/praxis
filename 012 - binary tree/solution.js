class No {
  val = null;
  left = null;
  right = null;

  constructor(val, left, right) {
    this.val = val;
    this.left = left;
    this.right = right;
  }
}

function goPreOrdemIter(root) {
  if (!root) return;
  let leftStack = [];
  let rightStack = [];
  leftStack.push(root);
  while (leftStack.length > 0 || rightStack.length > 0) {
    current = leftStack.pop() || rightStack.pop();
    console.log(current.val);
    if (current.left) leftStack.push(current.left);
    if (current.right) rightStack.push(current.right);
  }
}

function goPreOrdemRecur(root) {
  if (root == null) return;
  console.log(root.val);
  goPreOrdemRecur(root.left);
  goPreOrdemRecur(root.right);
}

function goOrdemIter(root) {
  console.log("don't know how to do")
}

function goOrdemRecur(root) {
  if (root == null) return;
  goPreOrdemRecur(root.left);
  console.log(root.val);
  goPreOrdemRecur(root.right);
}

n1 = new No(1);
n2 = new No(2);
n3 = new No(3, n1, n2);
n4 = new No(4);
n5 = new No(5, n3, n4);

console.log("goPreOrdemIter");
goPreOrdemIter(n5);

console.log("goPreOrdemRecur");
goPreOrdemRecur(n5);

console.log("goOrdemIter");
goOrdemIter(n5);

console.log("goOrdemRecur");
goOrdemRecur(n5);

// [ TODO ] - Depth and Breath