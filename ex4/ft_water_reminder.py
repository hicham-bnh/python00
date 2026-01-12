# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mobenhab <mobenhab@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/11 16:29:27 by mobenhab          #+#    #+#              #
#    Updated: 2026/01/12 14:00:44 by mobenhab         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_water_reminder():
   day = int(input("Days since last watering: "))
   if (day > 2) :
        print("Water the plants!")
   else :
        print("Plants are fine")
    