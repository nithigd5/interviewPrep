#include <stdio.h>

int main()
{
  int num;
  scanf("%d", &num);
  char lastDigitwords[][10] =
      {"Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
       "Nine"};
  char _2digitWords[][10] =
      {"Ten","Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
       "Seventeen", "Eighteen", "Nineteen"};
  char digitys[][10] =
      {"Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty",
       "Ninety"};

  int n = num;
  int nums[10];
  int d = 0;
  if (n == 0)
  {
    printf("Zero");
    return 0;
  }
  while (n != 0)
  {
    nums[d] = n % 10;
    n = n / 10;
    d++;
  }

  if (d == 1)
  {
    printf("%s ", lastDigitwords[nums[d-1]]);
  }
  if (d == 2)
  {
    if (nums[d-1] == 1)
    {
      printf("%s ", _2digitWords[nums[d-2]]);
    }
    else
    {
      printf("%s ", digitys[nums[d-1] - 2]);
      if (nums[d - 2] != 0)
        printf("%s ", lastDigitwords[nums[d - 2]]);
    }
  }
  if (d == 3)
  {
    printf("%s Hundred ", lastDigitwords[nums[d-1]]);
    d--;
    if (nums[d-1] == 1)
    {
      printf("%s ", _2digitWords[nums[d-2]]);
    }
    else
    {
      printf("%s ", digitys[nums[d-1] - 2]);
      if (nums[d - 2] != 0)
        printf("%s ", lastDigitwords[nums[d - 2]]);
    }
  }
  return 0;
}
