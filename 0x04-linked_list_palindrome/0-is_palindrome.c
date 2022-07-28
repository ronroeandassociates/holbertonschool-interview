#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to the head of the linked list
 * @tail: pointer to the tail of the linked list
 * is a palindrome
 * Return: 1 if the list is a palindrome, 0 otherwise
 */

int recursive_is_palindrome(listint_t *head, listint_t *tail)
{
  if (head == NULL)
    return (1);
  if (head->next == tail)
    return (1);
  if (head->n != tail->n)
    return (0);
  return (recursive_is_palindrome(head->next, tail->next));
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to the head of the linked list
 * is a palindrome
 * Return: 1 if the list is a palindrome, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
  listint_t *tail;

  if (head == NULL || *head == NULL)
    return (1);
  tail = *head;
  while (tail->next != NULL)
    tail = tail->next;
  return (recursive_is_palindrome(*head, tail));
}
