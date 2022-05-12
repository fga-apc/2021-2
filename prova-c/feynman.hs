import Control.Monad

main = do
    n <- readLn
    when (n /= 0) $ do
        let total = sum $ [ min i j | i <- [1..n], j <- [1..n] ]
        putStrLn $ show total
        main