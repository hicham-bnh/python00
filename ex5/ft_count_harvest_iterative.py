# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mobenhab <mobenhab@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/11 17:27:30 by mobenhab          #+#    #+#              #
#    Updated: 2026/01/11 17:28:02 by mobenhab         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative():
    day = 1
    last_day = input("Days until harvest: ")
    last_day = int(last_day)
    while day <= last_day:
        print("Day ", day)
        day+=1
    print("Harvest time!")