#include "palindrome.h"

/**
 * @brief   function that checks whether or not a given
 * unsigned integer is a palindrome.
 * Prototype: int is_palindrome(unsigned long n);
 * Where n is the number to be checked
 * Your function must return 1 if n is a palindrome, and 0 otherwise
 */

int is_palindrome(unsigned long n)
{
  unsigned long reverse = 0;
  unsigned long temp = n;
  if (n == 0)
    return 1;
  while (temp > 0)
  {
    reverse = reverse * 10 + temp % 10;
    temp /= 10;
  }
  return (n == reverse);
}
