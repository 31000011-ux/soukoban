function アイテムを与える() {
    player.execute("/give @p firework_rocket 256")
    player.execute("give @p bone")
    player.execute("give @p apple")
    player.execute("/give @p iron_shovel")
}

//  骨を使うと関数：初期化()が呼び出される
player.onItemInteracted(BONE, function on_item_interacted_bone() {
    初期化()
})
function ガラスとたいまつリセット() {
    //  倉庫内のガラスブロックを空気ブロックに変える。一旦、倉庫内のガラスブロックを消すイメージ
    blocks.replace(AIR, GLASS, world(7, -60, -12), world(0, -59, -16))
    //  ゴールすると花火の入った発射装置が起動する場所にレッドストーントーチがおかれるので、その場所を空気に置き換えて、花火をストップする。
    //  ゲームクリア後に、もう一度ゲームを再開したいときなどに必要となる処理。
    blocks.place(AIR, world(7, -60, -19))
}

//  リンゴを使うと関数：ガラスを動かす()、ゴール判定()が呼び出される
player.onItemInteracted(APPLE, function on_item_interacted_apple() {
    ガラスを動かす()
    ゴール判定()
})
//  鉄のシャベルを使うと、ゲームモードをクリエイティブモードに変える（倉庫番ゲームでは必要ないコード）
player.onItemInteracted(IRON_SHOVEL, function on_item_interacted_iron_shovel() {
    gameplay.setGameMode(CREATIVE, mobs.target(NEAREST_PLAYER))
})
function 初期化() {
    //  プレイヤーがスタート地点に移動
    player.teleport(world(6, -60, -12))
    ガラスとたいまつリセット()
    外枠レンガの設置()
    ガラスとゴールの設置()
    gameplay.title(mobs.target(NEAREST_PLAYER), "スタート", "3. りんごを持って右クリックでガラスを押す！")
    gameplay.setGameMode(ADVENTURE, mobs.target(NEAREST_PLAYER))
}

function 外枠レンガの設置() {
    builder.face(NORTH)
    builder.teleportTo(pos(1, 0, 0))
    builder.mark()
    builder.move(FORWARD, 2)
    for (let index = 0; index < 3; index++) {
        builder.move(LEFT, 1)
        builder.move(FORWARD, 1)
    }
    builder.move(LEFT, 4)
    builder.move(BACK, 3)
    for (let index2 = 0; index2 < 3; index2++) {
        builder.move(RIGHT, 1)
        builder.move(BACK, 1)
    }
    builder.move(RIGHT, 4)
    builder.raiseWall(BRICKS, 2)
}

function ガラスとゴールの設置() {
    //  ガラスブロックをスタート位置に置く
    blocks.fill(GLASS, world(4, -60, -13), world(5, -59, -13), FillOperation.Replace)
    //  ガラスブロックをスタート位置に置く
    blocks.fill(DIAMOND_BLOCK, world(1, -61, -16), world(2, -61, -16), FillOperation.Replace)
}

//  2箇所の地点（下がダイヤモンドブロック）にガラスブロックを移動させることが出来たら、発射装置が連続で花火を発射する動力起動部分にレッドストーントーチを置く。ゴールすると花火が打ち上がる。
function ゴール判定() {
    if (blocks.testForBlock(GLASS, world(1, -60, -16)) && blocks.testForBlock(GLASS, world(2, -60, -16))) {
        blocks.place(REDSTONE_TORCH, world(7, -60, -19))
    }
    
}

//  1つ前がガラスブロックで、2つ前が空気ブロックだったら、目の前のガラスブロック（2段分）を2つ前に移動させる。
//  リンゴを使ったときに、ガラスブロックの先にスペースが有れば、ガラスを前に押すイメージ
function ガラスを動かす() {
    if (blocks.testForBlock(GLASS, posCamera(0, 0, 1)) && blocks.testForBlock(AIR, posCamera(0, 0, 2))) {
        blocks.clone(posCamera(0, 0, 1), posCamera(0, 1, 1), posCamera(0, 0, 2), CloneMask.Replace, CloneMode.Move)
    }
    
}

function ゴール花火の設置() {
    builder.teleportTo(world(6, -60, -19))
    builder.face(WEST)
    builder.place(REDSTONE_WIRE)
    builder.move(FORWARD, 1)
    builder.place(blocks.comparator(WEST, ComparatorMode.Substract))
    builder.move(RIGHT, 1)
    builder.place(blocks.repeater(SOUTH, 2))
    builder.move(RIGHT, 1)
    builder.mark()
    builder.move(FORWARD, 1)
    builder.move(LEFT, 2)
    builder.move(FORWARD, 1)
    builder.tracePath(REDSTONE_WIRE)
    player.execute("fill 1 -60 -19 2 -60 -19 dispenser 1")
}

ゴール花火の設置()
アイテムを与える()
//  プレイヤーがスタート地点に移動
player.teleport(world(2, -60, -18))
gameplay.title(mobs.target(NEAREST_PLAYER), "倉庫番ゲーム", "ガラスを押して、ダイヤモンドの床まで動かしてね")
gameplay.title(mobs.target(NEAREST_PLAYER), "", "1. ディスペンサーに花火を入れて")
gameplay.title(mobs.target(NEAREST_PLAYER), "", "2. 骨を持って右クリックでスタート！")
