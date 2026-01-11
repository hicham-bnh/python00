# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mobenhab <mobenhab@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/11 16:20:54 by mobenhab          #+#    #+#              #
#    Updated: 2026/01/11 16:24:37 by mobenhab         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total():
    day1 = input("Day 1 harvest: ")
    day1 = int(day1)
    day2 = input("Day 2 harvest: ")
    day2 = int(day2)
    day3 = input("Day 3 harvest: ")
    day3 = int(day3)
    print("Total harvest: ", day1 + day2 + day3)