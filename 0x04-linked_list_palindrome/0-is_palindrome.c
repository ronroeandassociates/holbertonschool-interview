#include "lists.h"

/**
 * is_palindrome - checks if a number is a palindrome
 * @n: number to check
 *
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
  int length = list_length(head);
  int half_length = length / 2;
  int i, if_palindrome = 1;
  listint_t *reversed_head;
  listint_t *current = *head;
  listint_t *current_reversed;

  reversed_head = *head;
  for (i = 0; i < half_length; i++)
    reversed_head = reversed_head->next;
  if (length % 2 != 0)
    reversed_head = reversed_head->next;
  reversed_head = reversed(&reversed_head);
  current_reversed = reversed_head;
  current = *head;
  while (current_reversed != NULL)
  {
    if (current_reversed->n != current->n)
      if_palindrome = 0;
    current_reversed = current_reversed->next;
    current = current->next;
  }
  return (if_palindrome);
}
