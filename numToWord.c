#include<stdio.h>

int main ()
{
  int num;
  scanf ("%d", &num);
  char lastDigitwords[][10] =
    { "Zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
    "nine", "ten"
  };
  char _2digitWords[][10] =
    { "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
    "seventeen", "eighteen", "nineteen"
  };
  char digitys[][10] =
    { "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty",
    "ninety"
  };

  int n = num;
  int nums[10];
  int d = 0;
  if (n == 0)
    {
      printf ("zero");
      return 0;
    }
  while (n != 0)
    {
      *(nums + d) = n % 10;
      n = n / 10;
      d++;
    }
  d = d - 1;
  if (d == 0)
    {
      printf ("%s ", lastDigitwords[nums[d]]);
    }
  if (d == 2)
    {
      printf ("%s Hundred ", lastDigitwords[nums[d]]);
      d--;
    }
  if (d == 1)
    {
      if (nums[d] == 1)
	{
	  printf ("%s ", _2digitWords[nums[d]]);
	}
      else
	{
	  printf ("%s ", digitys[nums[d] - 2]);
	  if (nums[d - 1] != 0)
	    printf ("%s ", lastDigitwords[nums[d - 1]]);
	}

    }
  return 0;
}
