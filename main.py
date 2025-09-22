def アイテムを与える():
    player.execute("/give @p firework_rocket 256")
    player.execute("give @p bone")
    player.execute("give @p apple")
    player.execute("/give @p iron_shovel")
# 骨を使うと関数：初期化()が呼び出される

def on_item_interacted_bone():
    初期化()
player.on_item_interacted(BONE, on_item_interacted_bone)

def ガラスとたいまつリセット():
    # 倉庫内のガラスブロックを空気ブロックに変える。一旦、倉庫内のガラスブロックを消すイメージ
    blocks.replace(AIR, GLASS, world(7, -60, -12), world(0, -59, -16))
    # ゴールすると花火の入った発射装置が起動する場所にレッドストーントーチがおかれるので、その場所を空気に置き換えて、花火をストップする。
    # ゲームクリア後に、もう一度ゲームを再開したいときなどに必要となる処理。
    blocks.place(AIR, world(7, -60, -19))
# リンゴを使うと関数：ガラスを動かす()、ゴール判定()が呼び出される

def on_item_interacted_apple():
    ガラスを動かす()
    ゴール判定()
player.on_item_interacted(APPLE, on_item_interacted_apple)

# 鉄のシャベルを使うと、ゲームモードをクリエイティブモードに変える（倉庫番ゲームでは必要ないコード）

def on_item_interacted_iron_shovel():
    gameplay.set_game_mode(CREATIVE, mobs.target(NEAREST_PLAYER))
player.on_item_interacted(IRON_SHOVEL, on_item_interacted_iron_shovel)

def 初期化():
    # プレイヤーがスタート地点に移動
    player.teleport(world(6, -60, -12))
    ガラスとたいまつリセット()
    外枠レンガの設置()
    ガラスとゴールの設置()
    gameplay.title(mobs.target(NEAREST_PLAYER),
        "スタート",
        "3. りんごを持って右クリックでガラスを押す！")
    gameplay.set_game_mode(ADVENTURE, mobs.target(NEAREST_PLAYER))
def 外枠レンガの設置():
    builder.face(NORTH)
    builder.teleport_to(pos(1, 0, 0))
    builder.mark()
    builder.move(FORWARD, 2)
    for index in range(3):
        builder.move(LEFT, 1)
        builder.move(FORWARD, 1)
    builder.move(LEFT, 4)
    builder.move(BACK, 3)
    for index2 in range(3):
        builder.move(RIGHT, 1)
        builder.move(BACK, 1)
    builder.move(RIGHT, 4)
    builder.raise_wall(BRICKS, 2)
def ガラスとゴールの設置():
    # ガラスブロックをスタート位置に置く
    blocks.fill(GLASS,
        world(4, -60, -13),
        world(5, -59, -13),
        FillOperation.REPLACE)
    # ガラスブロックをスタート位置に置く
    blocks.fill(DIAMOND_BLOCK,
        world(1, -61, -16),
        world(2, -61, -16),
        FillOperation.REPLACE)
# 2箇所の地点（下がダイヤモンドブロック）にガラスブロックを移動させることが出来たら、発射装置が連続で花火を発射する動力起動部分にレッドストーントーチを置く。ゴールすると花火が打ち上がる。
def ゴール判定():
    if blocks.test_for_block(GLASS, world(1, -60, -16)) and blocks.test_for_block(GLASS, world(2, -60, -16)):
        blocks.place(REDSTONE_TORCH, world(7, -60, -19))
# 1つ前がガラスブロックで、2つ前が空気ブロックだったら、目の前のガラスブロック（2段分）を2つ前に移動させる。
# リンゴを使ったときに、ガラスブロックの先にスペースが有れば、ガラスを前に押すイメージ
def ガラスを動かす():
    if blocks.test_for_block(GLASS, pos_camera(0, 0, 1)) and blocks.test_for_block(AIR, pos_camera(0, 0, 2)):
        blocks.clone(pos_camera(0, 0, 1),
            pos_camera(0, 1, 1),
            pos_camera(0, 0, 2),
            CloneMask.REPLACE,
            CloneMode.MOVE)
def ゴール花火の設置():
    builder.teleport_to(world(6, -60, -19))
    builder.face(WEST)
    builder.place(REDSTONE_WIRE)
    builder.move(FORWARD, 1)
    builder.place(blocks.comparator(WEST, ComparatorMode.SUBSTRACT))
    builder.move(RIGHT, 1)
    builder.place(blocks.repeater(SOUTH, 2))
    builder.move(RIGHT, 1)
    builder.mark()
    builder.move(FORWARD, 1)
    builder.move(LEFT, 2)
    builder.move(FORWARD, 1)
    builder.trace_path(REDSTONE_WIRE)
    player.execute("fill 1 -60 -19 2 -60 -19 dispenser 1")
ゴール花火の設置()
アイテムを与える()
# プレイヤーがスタート地点に移動
player.teleport(world(2, -60, -18))
gameplay.title(mobs.target(NEAREST_PLAYER),
    "倉庫番ゲーム",
    "ガラスを押して、ダイヤモンドの床まで動かしてね")
gameplay.title(mobs.target(NEAREST_PLAYER), "", "1. ディスペンサーに花火を入れて")
gameplay.title(mobs.target(NEAREST_PLAYER), "", "2. 骨を持って右クリックでスタート！")