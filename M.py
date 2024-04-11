children = int(input())
candies = int(input())
candiesPerChild = candies // children
print(candiesPerChild)
print(candies - candiesPerChild * children)