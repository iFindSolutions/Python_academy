
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target

target = 9

nums = [2, 7, 11, 15]

def twosums(nums, target):

    h = {}
    for i, num in enumerate(nums):
        # print(i, num)
        n = target - num
        if n not in h:
            h[num] = i
        else:
            return [h[n], i]


print(twosums(nums, target))


# 290c34d22f6d6b86efe7f93771ed16ae1789a44c

# git remote -v
# git remote remove origin
# git remote add origin git@github.com:user/repo.git