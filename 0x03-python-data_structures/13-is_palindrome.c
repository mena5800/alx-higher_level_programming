#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to pointer of first node of listint_t list.
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	listint_t *new = *head;
	int *list_1, *list_2;
	int counter = 0;
	int half_counter = 0;
	int i;
	int check;

	if (current == NULL || current->next == NULL)
	{
		return (0);
	}
	while (current)
	{
		counter++;
		current = current->next;
	}
	half_counter = counter / 2;
	list_1 = malloc(half_counter * sizeof(int));
	list_2 = malloc(half_counter * sizeof(int));

	for (i = 0; i < half_counter; i++)
	{
		list_1[i] = new->n;
		new = new->next;
	}

	if (counter % 2 != 0)
		new = new->next;

	for (i = 0; i < half_counter; i++)
	{
		list_2[i] = new->n;
		new = new->next;
	}
	reverse(&list_2, half_counter);
	check = list_cmp(list_1, list_2, half_counter);
	free(list_1);
	free(list_2);
	return (check);
}

/**
 * list_cmp - function to comapre 2 lists
 * @list1: the first list
 * @list2: the second list
 * @counter: the length of list
 * Return: 1 if two lists identical and 0 if not
 */
int list_cmp(int *list1, int *list2, int counter)
{
	int i = 0;
	int flag = 1;

	for (i = 0; i < counter; i++)
	{
		if (list1[i] == list2[i])
		{
			continue;
		}
		else
		{
			flag = 0;
			break;
		}
	}
	return (flag);
}

/**
 * reverse - reverse list
 * @ptr: is pointer to pointer to list
 * @length: the length of list
 * Return: always one
 */
int reverse(int **ptr, int length)
{
	int *nums = *ptr;
	int last = length - 1;
	int temp;

	for (int i = 0; i < length / 2; i++)
	{
		temp = nums[i];
		nums[i] = nums[last];
		nums[last] = temp;
		last--;
	}
	return (1);
}
