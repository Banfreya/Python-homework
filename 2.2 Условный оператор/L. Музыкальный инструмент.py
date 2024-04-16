first_triangle_side = int(input())
second_triangle_side = int(input())
third_triangle_side = int(input())
if first_triangle_side + second_triangle_side > third_triangle_side \
    and first_triangle_side + third_triangle_side > second_triangle_side \
        and second_triangle_side + third_triangle_side > first_triangle_side:
    print("YES")
else:
    print("NO")
