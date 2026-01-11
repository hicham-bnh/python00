# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mobenhab <mobenhab@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/11 16:34:00 by mobenhab          #+#    #+#              #
#    Updated: 2026/01/11 16:48:18 by mobenhab         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_recursive(day):
    last_day = input("Days until harvest: ")
    last_day = int(last_day)
    day = 1
    if last_day == day:
        print("Harvest time!")
        return 0
    else:
            print("Day ",day)
            return(ft_count_harvest_recursive(day + 1))