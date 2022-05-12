nums = [*map(float, input().split())]
total = sum(nums)

if total <= 2 * max(nums):
    a, b, c = nums
    area = (a + b) * c / 2
    print(f"Area = {area:.1f}")
else:
    print(f"Perimetro = {total:.1f}")
