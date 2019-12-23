package main
import (
	"fmt"
	"time"
	"math/rand"
	"math/big"
)


func getKey(variable, private, p *big.Int) *big.Int {
	// variable: g for public key/public key for secret key
	mod := big.NewInt(0)
	return mod.Exp(variable, private, p)
}

func main() {
	rand.Seed(time.Now().UnixNano())

	g := big.NewInt(11)
	p := big.NewInt(rand.Int63())

	alicePrivateKey := big.NewInt(rand.Int63())
	bobPrivateKey := big.NewInt(rand.Int63())

	alicePublicKey := getKey(g, alicePrivateKey, p)
	bobPublicKey := getKey(g, bobPrivateKey, p)

	aliceSecretKey := getKey(bobPublicKey, alicePrivateKey, p)
	bobSecretKey := getKey(alicePublicKey, bobPrivateKey, p)

	fmt.Printf("alice private key: %v\n", alicePrivateKey)
	fmt.Printf("bob private key: %v\n", bobPrivateKey)
	fmt.Printf("alice public key: %v\n", alicePublicKey)
	fmt.Printf("bob public key: %v\n", bobPublicKey)
	fmt.Printf("secret keys: %v, %v\n", aliceSecretKey, bobSecretKey)
}
