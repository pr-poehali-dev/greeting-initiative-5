import { useState } from 'react';
import { Card } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Progress } from '@/components/ui/progress';
import { Badge } from '@/components/ui/badge';
import Icon from '@/components/ui/icon';

const Index = () => {
  const [messages, setMessages] = useState([
    { role: 'assistant', content: 'Привет! Я помогу запустить приложения Windows 10 на твоей Windows 7. Что нужно сделать?' }
  ]);
  const [input, setInput] = useState('');
  const [systemStatus, setSystemStatus] = useState({
    compatibility: 75,
    updates: 45,
    libraries: 90
  });

  const handleSend = () => {
    if (!input.trim()) return;
    
    setMessages([...messages, 
      { role: 'user', content: input },
      { role: 'assistant', content: 'Анализирую приложение... Настраиваю параметры совместимости для запуска на Windows 7.' }
    ]);
    setInput('');
  };

  return (
    <div className="min-h-screen bg-background dark p-6">
      <div className="max-w-7xl mx-auto">
        <div className="mb-8">
          <div className="flex items-center gap-3 mb-2">
            <div className="w-12 h-12 bg-primary rounded-2xl flex items-center justify-center">
              <Icon name="Bot" size={28} className="text-primary-foreground" />
            </div>
            <div>
              <h1 className="text-3xl font-bold text-foreground">Windows AI Assistant</h1>
              <p className="text-muted-foreground">Запуск приложений Windows 10 на Windows 7</p>
            </div>
          </div>
        </div>

        <div className="grid lg:grid-cols-3 gap-6">
          <div className="lg:col-span-2">
            <Card className="bg-card border-border overflow-hidden">
              <div className="h-[600px] flex flex-col">
                <div className="flex-1 p-6 overflow-y-auto space-y-4">
                  {messages.map((msg, idx) => (
                    <div
                      key={idx}
                      className={`flex gap-3 ${msg.role === 'user' ? 'justify-end' : 'justify-start'} animate-fade-in`}
                    >
                      {msg.role === 'assistant' && (
                        <div className="w-10 h-10 bg-primary/10 rounded-xl flex items-center justify-center flex-shrink-0">
                          <Icon name="Bot" size={20} className="text-primary" />
                        </div>
                      )}
                      <div
                        className={`max-w-[80%] rounded-2xl px-4 py-3 ${
                          msg.role === 'user'
                            ? 'bg-primary text-primary-foreground'
                            : 'bg-muted text-muted-foreground'
                        }`}
                      >
                        {msg.content}
                      </div>
                      {msg.role === 'user' && (
                        <div className="w-10 h-10 bg-accent/20 rounded-xl flex items-center justify-center flex-shrink-0">
                          <Icon name="User" size={20} className="text-accent" />
                        </div>
                      )}
                    </div>
                  ))}
                </div>

                <div className="border-t border-border p-4">
                  <div className="flex gap-3">
                    <Input
                      value={input}
                      onChange={(e) => setInput(e.target.value)}
                      onKeyPress={(e) => e.key === 'Enter' && handleSend()}
                      placeholder="Напиши, какое приложение нужно запустить..."
                      className="flex-1 bg-muted border-border text-foreground placeholder:text-muted-foreground"
                    />
                    <Button onClick={handleSend} className="bg-primary hover:bg-primary/90 text-primary-foreground">
                      <Icon name="Send" size={20} />
                    </Button>
                  </div>
                </div>
              </div>
            </Card>
          </div>

          <div className="space-y-6">
            <Card className="bg-card border-border p-6">
              <div className="flex items-center gap-2 mb-6">
                <Icon name="Activity" size={24} className="text-primary" />
                <h2 className="text-xl font-semibold text-foreground">Статус системы</h2>
              </div>

              <div className="space-y-6">
                <div>
                  <div className="flex items-center justify-between mb-2">
                    <span className="text-sm text-muted-foreground">Совместимость</span>
                    <Badge className="bg-primary/20 text-primary border-0">{systemStatus.compatibility}%</Badge>
                  </div>
                  <Progress value={systemStatus.compatibility} className="h-2" />
                </div>

                <div>
                  <div className="flex items-center justify-between mb-2">
                    <span className="text-sm text-muted-foreground">Обновления</span>
                    <Badge className="bg-accent/20 text-accent border-0">{systemStatus.updates}%</Badge>
                  </div>
                  <Progress value={systemStatus.updates} className="h-2" />
                </div>

                <div>
                  <div className="flex items-center justify-between mb-2">
                    <span className="text-sm text-muted-foreground">Библиотеки</span>
                    <Badge className="bg-primary/20 text-primary border-0">{systemStatus.libraries}%</Badge>
                  </div>
                  <Progress value={systemStatus.libraries} className="h-2" />
                </div>
              </div>
            </Card>

            <Card className="bg-card border-border p-6">
              <div className="flex items-center gap-2 mb-4">
                <Icon name="Settings" size={24} className="text-primary" />
                <h2 className="text-xl font-semibold text-foreground">Быстрые действия</h2>
              </div>

              <div className="space-y-3">
                <Button 
                  variant="outline" 
                  className="w-full justify-start gap-3 border-border hover:bg-muted text-foreground"
                >
                  <Icon name="Download" size={18} className="text-primary" />
                  Установить обновления
                </Button>
                
                <Button 
                  variant="outline" 
                  className="w-full justify-start gap-3 border-border hover:bg-muted text-foreground"
                >
                  <Icon name="Shield" size={18} className="text-accent" />
                  Режим совместимости
                </Button>
                
                <Button 
                  variant="outline" 
                  className="w-full justify-start gap-3 border-border hover:bg-muted text-foreground"
                >
                  <Icon name="RefreshCw" size={18} className="text-primary" />
                  Обновить библиотеки
                </Button>
              </div>
            </Card>

            <Card className="bg-card border-border p-6">
              <div className="flex items-center gap-2 mb-4">
                <Icon name="Clock" size={24} className="text-primary" />
                <h2 className="text-xl font-semibold text-foreground">Недавние запуски</h2>
              </div>

              <div className="space-y-3">
                {['Discord.exe', 'Telegram.exe', 'Chrome 120'].map((app, idx) => (
                  <div key={idx} className="flex items-center justify-between py-2 border-b border-border last:border-0">
                    <div className="flex items-center gap-3">
                      <div className="w-8 h-8 bg-primary/10 rounded-lg flex items-center justify-center">
                        <Icon name="Package" size={16} className="text-primary" />
                      </div>
                      <span className="text-sm text-foreground">{app}</span>
                    </div>
                    <Badge variant="outline" className="bg-primary/5 text-primary border-primary/20">
                      Успешно
                    </Badge>
                  </div>
                ))}
              </div>
            </Card>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Index;
