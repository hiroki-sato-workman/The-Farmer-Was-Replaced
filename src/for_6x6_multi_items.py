# 6x6マスで干し草、木、人参を収穫するロジック

clear()

count = 0
worldSize = get_world_size()

# 茂み＆木ライン
def is_bush_line() -> bool:
	return get_pos_x() == 2 or get_pos_x() == 3
# 人参ライン
def is_carrot_line():
	return get_pos_x() == 4 or get_pos_x() == 5

# 茂みを植える関数
def plant_bush():
	if is_bush_line():
		#plant(Entities.Tree)
		if is_bush_line():
			# 偶数行の場合
			if get_pos_y() % 2 == 0:
				# 偶数列の場合
				if get_pos_x() % 2 == 0:
					plant(Entities.Tree)
				# 奇数列の場合
				else:
					plant(Entities.Bush)
			# 奇数行の場合
			else:
				# 偶数列の場合
				if get_pos_x() % 2 == 0:
					plant(Entities.Bush)
				# 奇数列の場合
				else:
					plant(Entities.Tree)

# 人参を植える関数
def plant_carrot():
	if is_carrot_line():
		# 初回実行時のみ耕す
		if count == 1:
			till()
 		# 人参を植える
		plant(Entities.Carrot)

# 収穫をする
def do_hervest():
	if can_harvest():
		harvest()
		# 茂みの場合
		if is_bush_line():
			plant_bush()
			
		# 人参の場合
		if is_carrot_line():
			plant_carrot()
			
# 横移動と各作物を植える
def move_x(x_index):
	for y_index in range(worldSize):
		# 茂みの場合
		plant_bush()
		# 人参の場合
		plant_carrot()
		# 水を撒く
		if get_water() < 0.1:
			use_item(Items.Water)		
		# 収穫する
		do_hervest()

		# 移動処理
		move(North)
		if y_index == worldSize - 1:
			move(East)

# メインロジック
while True:
	count += 1
	for i in range(worldSize):
		move_x(i)
