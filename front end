import { useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";
import { Sun, Moon } from "lucide-react";

export default function TradingDashboard() {
  const [darkMode, setDarkMode] = useState(true);
  const [showSidePanels, setShowSidePanels] = useState(true);
  const data = [
    { time: "10:00", price: 40000 },
    { time: "10:30", price: 40500 },
    { time: "11:00", price: 39800 },
    { time: "11:30", price: 41000 },
    { time: "12:00", price: 41500 },
  ];

  return (
    <div className={`min-h-screen p-4 ${darkMode ? "bg-gray-900 text-white" : "bg-white text-black"}`}>
      <div className="flex justify-between items-center mb-4">
        <h1 className="text-xl font-bold">Trading Dashboard</h1>
        <div className="flex gap-2">
          <Button onClick={() => setShowSidePanels(!showSidePanels)}>
            Toggle Side Panels
          </Button>
          <Button onClick={() => setDarkMode(!darkMode)}>
            {darkMode ? <Sun /> : <Moon />}
          </Button>
        </div>
      </div>

      <div className="grid grid-cols-12 gap-4">
        {showSidePanels && (
          <Card className="col-span-3 p-4">
            <h2 className="text-lg font-semibold mb-2">Market Data</h2>
            <p>BTC/USDT: $41,500</p>
            <p>ETH/USDT: $3,200</p>
          </Card>
        )}

        <Card className="col-span-6 p-4">
          <h2 className="text-lg font-semibold mb-2">Trading Chart</h2>
          <ResponsiveContainer width="100%" height={300}>
            <LineChart data={data}>
              <XAxis dataKey="time" stroke={darkMode ? "#fff" : "#000"} />
              <YAxis stroke={darkMode ? "#fff" : "#000"} />
              <Tooltip />
              <Line type="monotone" dataKey="price" stroke="#4F46E5" strokeWidth={2} />
            </LineChart>
          </ResponsiveContainer>
        </Card>

        {showSidePanels && (
          <Card className="col-span-3 p-4">
            <h2 className="text-lg font-semibold mb-2">Trade Execution</h2>
            <Button className="w-full mb-2 bg-green-500 hover:bg-green-700">Buy</Button>
            <Button className="w-full bg-red-500 hover:bg-red-700">Sell</Button>
          </Card>
        )}
      </div>
    </div>
  );
}
