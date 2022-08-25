#include "lists.h"
/**
 * check_cycle - Verify if a list has a cycle in it or not
 * @list: list where we verify
 *
 * Return: 1 if yes
 * 0 if no
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp = NULL;
	listint_t *head =NULL;

	if(list != NULL)
	{
		head = list;
		tmp = list->next;
		while (tmp != NULL && head && tmp->next)
		{
			if (tmp == head)
			{
				return (1);
			}
			tmp = tmp->next->next;
			head = head->next;
		}
	}
	return (0);
}
