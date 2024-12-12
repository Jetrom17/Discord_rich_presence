// Versão GO

package main

import (
	"fmt"
	"time"

	"github.com/hugolgst/rich-go/client"
	"github.com/shirou/gopsutil/cpu"
	"github.com/shirou/gopsutil/mem"
)

func main() {
	// Configuração inicial do cliente
	clientID := "51235641261243654" // Substitua pelo ID real

	err := client.Login(clientID)
	if err != nil {
		fmt.Println("Erro ao conectar ao cliente RPC:", err)
		return
	}

	start := time.Now()
	fmt.Println("Atualizando presença...")

	for {
		// Uso de CPU e RAM
		cpuUsage, _ := cpu.Percent(0, false)
		ramUsage, _ := mem.VirtualMemory()

		// Configurando a presença
		err = client.SetActivity(client.Activity{
			State:      fmt.Sprintf("CPU: %.1f%%, RAM: %.1f%%", cpuUsage[0], ramUsage.UsedPercent),
			Details:    "Sabedoria diária, que transforma sua vida!",
			Timestamps: &client.Timestamps{Start: &start},
			LargeImage: "https://i.imgur.com/aHOM9Tk.png",
			LargeText:  fmt.Sprintf("Uso de CPU: %.1f%%", cpuUsage[0]),
			SmallText:  fmt.Sprintf("Uso de RAM: %.1f%%", ramUsage.UsedPercent),
			Buttons: []*client.Button{
				{
					Label: "Método Destiny",
					Url:   "https://proverb-day.pages.dev/",
				},
			},
		})
		if err != nil {
			fmt.Println("Erro ao atualizar a presença:", err)
		}

		time.Sleep(5 * time.Second) // Atualiza a cada 5 segundos

		if time.Since(start) >= 24*time.Hour {
			break
		}
	}

	client.Logout()
}
