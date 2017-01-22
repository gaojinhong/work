# !/bin/usr/env python 3
# _*_ coding: utf-8 _*_
"""编写一个游戏，名为外星人入侵，需要设定：
1 一艘可以在底部自由移动的飞船
2 一组不断下移的外星人，外星人移动到底部或者接触到飞船，游戏失败
3 飞船可以发射子弹，消灭外星人
"""

import pygame

from pygame.sprite import Group

from settings import Settings

from game_stats import GameStats

from scoreboard import Scoreboard

from button import Button

from ship import Ship

import game_functions as gf

def run_game():
	#初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
	(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	#创建一个用于存储游戏统计信息的实例,并创建计分牌
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)
	
	#创建一艘飞船
	ship = Ship(ai_settings, screen)
	
	#创建一个用于存储子弹的编组
	bullets = Group()
	
	#创建一个外星人群的编组
	aliens = Group()
	
	#创建外星人群
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	#创建Play按钮
	play_button = Button(ai_settings, screen, "Play")
	
	#开始游戏的主循环
	while True:
	
		#监视键盘和鼠标事件
		gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
			gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
		
		#更新屏幕上的图像，并切换到新屏幕
		gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
		
run_game()
