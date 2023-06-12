#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to pointer of first node of listint_t list.
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int flag = 1, i, counter = 0;
	int *stack;

	if (current == NULL || current->next == NULL)
	{
		return (1);
	}
	while (current)
	{
		counter++;
		current = current->next;
	}
	stack = malloc((counter / 2) * sizeof(int));
	current = *head;
	for (i = 0; i < counter / 2; i++)
	{
		stack[i] = current->n;
		current = current->next;
	}
	if (counter % 2 != 0)
		current = current->next;
	for (i = counter / 2 - 1; i >= 0; i--)
	{
		if (stack[i] != current->n)
		{
			flag = 0;
			break;
		}
		current = current->next;
	}
	free(stack);
	return (flag);
}
