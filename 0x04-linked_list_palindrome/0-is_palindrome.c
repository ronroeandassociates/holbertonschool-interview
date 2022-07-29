#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to the head of the linked list
 * @tail: pointer to the tail of the linked list
 * is a palindrome
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int recursive(listint_t **head, listint_t *tail)
{
  int isPAlindrome;

  if (!tail)
    return (1);

  isPAlindrome = recursive(head, tail->next) && ((*head)->n == tail->n);
  if (!isPAlindrome)
    return (0);

  *head = (*head)->next;

  return (isPAlindrome);
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: pointer to the head of the linked list
 * is a palindrome
 * Return: 1 if the list is a palindrome, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
  return (recursive(head, *head));
}
