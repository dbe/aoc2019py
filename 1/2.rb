def cost(amt)
  needed = (amt / 3) - 2
  if needed <= 0
    return 0
  else
    return needed + cost(needed)
  end
end

def run(lines)
  return (lines.map {|e| cost e }).reduce(0, :+)
end

lines = File.read('1/in.txt').split.map {|line| line.to_i }
puts run lines
