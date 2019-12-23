package main
import (
	"fmt"
	"time"
	"math/rand"
	"math/big"
)


func getSecretKey(public, private, p *big.Int) *big.Int {
	secret := big.NewInt(0)
	return secret.Exp(public, private, p)
}

func getPublicKey(g, private, p *big.Int) *big.Int {
	mod := big.NewInt(0)
	return mod.Exp(g, private, p)
}

func main() {
	rand.Seed(time.Now().UnixNano())

	g := big.NewInt(11)
	p := big.NewInt(rand.Int63())

	alicePrivateKey := big.NewInt(rand.Int63())
	bobPrivateKey := big.NewInt(rand.Int63())

	alicePublicKey := getPublicKey(g, alicePrivateKey, p)
	bobPublicKey := getPublicKey(g, bobPrivateKey, p)

	aliceSecretKey := getSecretKey(bobPublicKey, alicePrivateKey, p)
	bobSecretKey := getSecretKey(alicePublicKey, bobPrivateKey, p)

	fmt.Printf("alice private key: %v\n", alicePrivateKey)
	fmt.Printf("bob private key: %v\n", bobPrivateKey)
	fmt.Printf("alice public key: %v\n", alicePublicKey)
	fmt.Printf("bob public key: %v\n", bobPublicKey)
	fmt.Printf("secret keys: %v, %v\n", aliceSecretKey, bobSecretKey)
}
