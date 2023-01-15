function [fib, ratio] = Fibonacci(n)
  clc; close;
  fib(1)=1;
  fib(2)=1;
  for i=2:n-1
    fib(i+1)=fib(i)+fib(i-1);
    ratio(i,:)=fib(i)/fib(i-1);

  end
  ratio(n,:)=fib(n)/fib(n-1);
  N = [1:n];
  cumulFib = cumsum(fib);
  summary = [fib',cumulFib', ratio]

  fig1 = figure(1);
  txt =  ['Fibonacci sequence '];
  txt2 =  ['Cumulative Fibonacci sequence '];
  plot(N,fib', '.k','MarkerSize',15,'DisplayName', txt)
  hold on
  plot(N,cumulFib', '.r', 'MarkerSize',15,'DisplayName', txt2)
  xlabel('Sequence number')
  ylabel('Sequence Value')
  axis([1 n+1 0 max(cumulFib)*1.1]);
  legend('location', 'northwest', 'fontsize', 12);
  legend show
  legend boxoff

  fig2 = figure(2);
  plot(N,ratio', '-b')
  hold on
  phi = 1.618034;
  plot([1:n],[ones(n)*phi], '--k')
  axis([1 n+1 0 max(ratio)*1.1]);

  print (fig1, "Fibonacci.png");
  print (fig2, "golden_ratio.png");
